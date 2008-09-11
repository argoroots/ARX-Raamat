<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Tags_model extends Model {

	function Tags_model() {
		parent::Model();
	}

	function find($tagtype = null, $show_values = false) {
		
		if($tagtype) {
			$tagtype_where = 'WHERE tagtypes.name = \''. $tagtype .'\'';
		} else {
			$tagtype_where = '';
		}

		$tagtypes = $this->db->query('
		SELECT SQL_CALC_FOUND_ROWS
			tagtypes.id,
			tagtypes.name,
			tags.values_count,
			tags.item_count
		FROM tagtypes
		LEFT JOIN (
			SELECT
				tagtype_id,
				COUNT(DISTINCT value) AS values_count,
				COUNT(DISTINCT media_id) AS item_count
			FROM tags
			WHERE media_id IN (SELECT media_id FROM items WHERE library_id IN('. $this->session->lib_list1 .'))
			GROUP BY tagtype_id
		) AS tags ON tags.tagtype_id = tagtypes.id
		'. $tagtype_where .'
		ORDER BY tagtypes.sortorder
		');

		//leitud ridade arv
		$row_count = $this->db->query('SELECT FOUND_ROWS() AS row_count;')->row()->row_count;

		foreach ($tagtypes->result_array() as $row) {

			$data[$row['id']] = $row;
			unset($data[$row['id']]['id']);
			
			if($show_values == true) {
				$tagvalues = $this->db->query('
				SELECT
					value,
					COUNT(media_id) item_count
				FROM tags
				WHERE tagtype_id = '. $row['id'] .'
				AND media_id IN (SELECT media_id FROM items WHERE library_id IN('. $this->session->lib_list1 .'))
				GROUP BY value
				ORDER BY value
				');
				unset($values_array);
				foreach ($tagvalues->result_array() as $values) {
					 $values_array[$values['value']] = $values['item_count'];
				}

				if(isset($values_array)) {
					$data[$row['id']]['values'] = $values_array;
				} else {
					$data[$row['id']]['values'] = null;
				}

			}

		}

		$vastus['row_count'] = $row_count;

		if(isset($data)) $vastus['data'] = $data; 
		
		return $vastus;

	}

}

?>
