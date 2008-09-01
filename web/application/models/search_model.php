<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Search_model extends Model {

	var $title   = '';
	var $content = '';
	var $date    = '';

	function Search_model() {
		parent::Model();
	}
	
	function find4($filter = null, $page = null, $result_per_page = null, $show_tags = false, $show_items = false) {

	}

}


?>
