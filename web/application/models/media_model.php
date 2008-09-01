<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Media_model extends Model {

	var $title   = '';
	var $content = '';
	var $date    = '';

	function Media_model() {
		parent::Model();
	}
	
	function find($filter = null, $page = null, $result_per_page = null, $show_tags = false, $show_items = false) {
		
		//et sisendandmed oleks OK
		if(!is_numeric($page)) $page = 1;
		if(!is_numeric($result_per_page)) $result_per_page = 50;
		
		
		if(is_array($filter)) {
			
			$where = '';
			$type = ($filter['type']=='all') ? 'AND' : 'OR';
			
			foreach($filter['search'] as $filter_row) {
				switch ($filter_row['operator']) {
					case 'contains':
						$where_op = ' LIKE \'%'. $filter_row['value'] .'%\'';
					  break;
					case 'doesnotcontain':
						$where_op = ' NOT LIKE \'%'. $filter_row['value'] .'%\'';
					  break;
					case 'is':
						$where_op = ' = \''. $filter_row['value'] .'\'';
					  break;
					case 'isnot':
						$where_op = ' != \''. $filter_row['value'] .'\'';
					  break;
					case 'startswith':
						$where_op = ' LIKE \''. $filter_row['value'] .'%\'';
					  break;
					case 'endswith':
						$where_op = ' LIKE \'%'. $filter_row['value'] .'\'';
					  break;
					default:
						$where_op = ' = \''. $filter_row['value'] .'\'';
				}

				switch ($filter_row['tagtype']) {
					case 'id':
						$where .= $type .' media.id '. $where_op;
					  break;
					case 'title':
						$where .= $type .' media.title '. $where_op;
					  break;
					case 'type_id':
						$where .= $type .' media.id IN (SELECT media_id FROM media_tags WHERE tag_id = (SELECT tag_id FROM media_tags WHERE id '. $where_op .'))';
					  break;
					case 'type':
						$where .= $type .' media.id IN (SELECT media_id FROM media_tags WHERE tag_id IN (SELECT id FROM tags WHERE name '. $where_op .' AND tagtype_id = 3))';
					  break;
					default:
						$where .= $type .' 1 = 2 ';
				}
			}
			
			$where = substr($where,3);

			//meedia leidmine
			$media = $this->db->query('
			SELECT DISTINCT SQL_CALC_FOUND_ROWS
				media.id,
				media.title,
				media.note
			FROM media
			WHERE media.id IN (SELECT media_id FROM items WHERE library_id IN('. $this->session->lib_list1 .'))
			AND ('. $where .')
			ORDER BY title
			LIMIT '. (($page-1) * $result_per_page) .', '. $result_per_page .'
			');
		} else {
			$filter = addslashes($filter);
			
			$match0 = 'MATCH (media.title) AGAINST (\''. $filter .'\' IN BOOLEAN MODE)';
			$match0_field = $match0 .' AS score, ';
			$match0_where = 'AND '. $match0;

			$match1 = 'MATCH (persons.lastname, persons.firstname) AGAINST (\''. $filter .'\' IN BOOLEAN MODE)';
			$match1_field = $match1 .' AS score, ';
			$match1_where = 'AND '. $match1;
			
			$match2 = 'MATCH (tags.name) AGAINST (\''. $filter .'\' IN BOOLEAN MODE)';
			$match2_field = $match2 .' AS score, ';
			$match2_where = 'AND '. $match2;
			
			$match_orderby = ' score DESC, ';
		
			//meedia leidmine
			$media = $this->db->query('
				SELECT DISTINCT SQL_CALC_FOUND_ROWS
					'. $match0_field .'
					media.id,
					media.title,
					media.note,
					0 AS query
				FROM media
				WHERE media.id IN (SELECT media_id FROM items WHERE library_id IN('. $this->session->lib_list1 .'))
				'. $match0_where .'
				UNION SELECT DISTINCT
					'. $match1_field .'
					media.id,
					media.title,
					media.note,
					1 AS query
				FROM
					media,
					media_persons,
					persons
				WHERE media_persons.media_id = media.id
				AND persons.id = media_persons.person_id
				AND media.id IN (SELECT media_id FROM items WHERE library_id IN('. $this->session->lib_list1 .'))
				'. $match1_where .'
				UNION SELECT DISTINCT
					'. $match2_field .'
					media.id,
					media.title,
					media.note,
					2 AS query
				FROM
					media,
					media_tags,
					tags
				WHERE media_tags.media_id = media.id
				AND tags.id = media_tags.tag_id
				AND media.id IN (SELECT media_id FROM items WHERE library_id IN('. $this->session->lib_list1 .'))
				'. $match2_where .'
				ORDER BY query, '. $match_orderby .'title
				LIMIT '. (($page-1) * $result_per_page) .', '. $result_per_page .'
			');
		}
		//leitud ridade arv
		$row_count = $this->db->query('SELECT FOUND_ROWS() AS row_count;')->row()->row_count;

		//käime leitud meedia read läbi ja võteme iga rea juurde andmed
		foreach ($media->result_array() as $row) {
			
			//loeme tagid kui tahetakse
			if($show_tags==true) {
				$tags = $this->db->query('
					SELECT
						media_tags.id,
						tagtypes.sortorder,
						tagtypes.name AS tag,
						tags.name AS value
					FROM
						media_tags,
						tags,
						tagtypes
					WHERE tags.id = media_tags.tag_id
					AND tagtypes.id = tags.tagtype_id
					AND media_tags.media_id = '. $row['id'] .'
					UNION SELECT
						media_persons.id,
						tagtypes.sortorder,
						tagtypes.name AS tag,
						CONCAT(persons.firstname, \' \', persons.lastname) AS value
					FROM
						media_persons,
						persons,
						tagtypes
					WHERE persons.id = media_persons.person_id
					AND tagtypes.id = media_persons.tagtype_id
					AND media_persons.media_id = '. $row['id'] .'
					ORDER BY sortorder, value
				');
				
				//loeme tagid arraysse
				unset($tags_array);
				foreach ($tags->result() as $tag) {
					$tags_array[$tag->tag][$tag->id] = $tag->value;
				}
			}
			
			//loeme itemite info kui tahetakse
			if($show_items==true) {
				$items = $this->db->query('
					SELECT
						id,
						item_number,
						barcode,
						quantity,
						price,
						note
					FROM
						items
					WHERE media_id = '. $row['id'] .'
				');
				
				//loeme itemid arraysse
				unset($items_array);
				foreach ($items->result_array() as $item) {
					$items_array[$item['id']] = $item;
					unset($items_array[$item['id']]['id']);
				}
			}
			
			$data[$row['id']] = $row;
			unset($data[$row['id']]['id']);
			if(isset($tags_array)) $data[$row['id']]['tags'] = $tags_array;
			if(isset($items_array)) $data[$row['id']]['items'] = $items_array;
			
			
		}
		
		$vastus['current_page'] = $page;
		$vastus['page_count'] = ceil($row_count / $result_per_page);
		$vastus['row_count'] = $row_count;

		if(isset($data)) $vastus['data'] = $data; 
		
		return $vastus;
	}

	function title_list($filter = null, $result_count = null) {
		
		//et sisendandmed oleks OK
		if(!is_numeric($result_count)) $result_per_page = 50;
		
		$filter = addslashes($filter);
		$match = 'MATCH (media.title) AGAINST (\''. $filter .'\' IN BOOLEAN MODE)';
		$match_field = $match .' AS score, ';
		$match_where = 'AND '. $match;
		$match_orderby = ' score DESC, ';
		
		//meedia leidmine
		$media = $this->db->query('
			SELECT DISTINCT
				'. $match_field .'
				media.id,
				media.title
			FROM
				media
			WHERE media.id IN (SELECT media_id FROM items WHERE library_id IN('. $this->session->lib_list1 .'))
			'. $match_where .'
			ORDER BY '. $match_orderby .'media.title
			LIMIT 0, '. $result_count .'
			');
		
		//käime leitud meedia read läbi ja võteme iga rea juurde andmed
		$data = array();
		foreach ($media->result() as $row) {

			$data[$row->id] = $row->title;

		}

		return $data;
	}

}

?>