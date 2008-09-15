<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Tags_model extends Model {

	function Tags_model() {
		parent::Model();
	}

//Tagastab tagide tüüpide array
	function get_tags() {
		
		$tagtypes = $this->db->query('
		SELECT
			id,
			name
		FROM
			tagtypes
		ORDER BY sortorder
		');

		$vastus = $tagtypes->result_array();

		return $vastus;

	}




//Tagastab etteantud tagi erinevate väärtuste array
	function get_tagvalues($tagtypeid = null) {
		
		$tagtype_where = ($tagtypeid) ? 'AND tags.tagtype_id = '. $tagtypeid : '';

		$tagvalues = $this->db->query('
		SELECT DISTINCT
			tagtypes.name AS tagtype,
			tags.value
		FROM
			tags,
			tagtypes
		WHERE tagtypes.id = tags.tagtype_id
		'. $tagtype_where .'
		AND tags.media_id IN (SELECT media_id FROM items WHERE library_id IN('. $this->session->lib_list1 .'))
		ORDER BY tags.value
		');

		$vastus = $tagvalues->result_array();

		return $vastus;

	}

}

?>
