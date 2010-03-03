<?php if(!defined('BASEPATH')) exit('No direct script access allowed');

/*

ARX-Raamatu disainisnipetite klass

*/

class Arxui {

	function Arxui() {

		//CI klassi kasutamine
		$this->CI =& get_instance();
		$this->CI->load->database();

	}



//Tagastab footeri nupud
	function footer_button($buttons, $style = '') {
	
		foreach($buttons as $key => $value) {
			$vastus_array[] = '<td><a href="'. $key .'">'. $value .'</a></td>';
		}
		
		$vastus = '
			<table class="footer_button" cellspacing="0" cellpadding="0" style="'. $style .'">
				<tr valign="top">
					<td><img src="'. site_url('images/footer_button_left.png') .'" alt="" /></td>
			';
		
		$vastus .= implode('<td><img src="'. site_url('images/footer_button_separator.png') .'" alt="" /></td>', $vastus_array);
		
		$vastus .= '
					<td><img src="'. site_url('images/footer_button_right.png') .'" alt="" /></td>
				</tr>
			</table>
			';
	
		return $vastus;
	
	}



//tagastab library vaates meedia tagide lingid
	function tag_links($tagtype, $tags_array) {
	
		foreach($tags_array as $key => $value) {
			$vastus_array[] = '<a href="'. site_url('library/search/'. rawurlencode(serialize(array('type'=>'all','search'=>array(array('tagtype'=>$tagtype, 'operator'=>'is', 'value'=>$value)))))) .'">'. $value .'</a>';
			//$vastus_array[] = '<a href="'. site_url('tags/'. $tagtype .'/'. $key) .'">'. $value .'</a>';
			//$vastus_array[] = '<a href="'. site_url('tags/show/'. $tagtype .'/'. $key) .'">'. $value .'</a>';
		}
	
		$vastus = implode(', ', $vastus_array);
		
		return $vastus;
	
	}



//tagastab filtri
	function searchbox($filter_array) {
		
		$vastus = '';

		$rownum = 1;
		$rowcount = count($filter_array['search']);
		$addnew = false;

		$vastus .= '<table cellspacing="0" cellpadding="0" align="center"><tr><td>';
		$vastus .= '<form id="search" action="'. site_url('library/submit_search') .'" method="post" style="margin:0px;"><fieldset>';

		$searxctype = '<select class="search" name="search_type">';
		$searxctype .= $this->_operator_option('any', $filter_array['type']);
		$searxctype .= $this->_operator_option('all', $filter_array['type']);
		$searxctype .= '</select> ';
		
		$vastus .= '<b>'. $this->CI->lang1->str('machallanyrules', $searxctype) .':</b>';

		foreach($filter_array['search'] as $filter_row) {
			if($rownum==$rowcount) $addnew = true;
			$vastus .= $this->add_searchbox($rownum, $filter_row['tagtype'], $filter_row['operator'], $filter_row['value'], $addnew);
			$rownum += 1;
		}
	
		$vastus .= '<input type="submit" class="search" name="search_submit" value="'. $this->CI->lang1->str('search') .'" style="float:right;" />';
		$vastus .= '</fieldset></form></td></tr></table>';

		return $vastus;
		
	}

	function add_searchbox($rownum, $tagtype = '', $operator = '', $value = '', $addnew = true) {
		
		$vastus = '';

		$tags = $this->CI->db->query('
			SELECT
				name,
				type
			FROM
				tagtypes
			ORDER BY sortorder
			')->result_array();
		
		//tagi tyypide list
		$taglist = '<select class="search" name="search_tagtype['. $rownum .']">';
		$taglist .= $this->_tagtype_option('title', $tagtype);
		foreach($tags as $tag) {
			$taglist .= $this->_tagtype_option($tag['name'], $tagtype);
		}
		$taglist .= '</select> ';

		//operaatorite list
		$operatorlist = '<select class="search" name="search_operator['. $rownum .']">';
		$operatorlist .= $this->_operator_option('contains', $operator);
		$operatorlist .= $this->_operator_option('doesnotcontain', $operator);
		$operatorlist .= $this->_operator_option('is', $operator);
		$operatorlist .= $this->_operator_option('isnot', $operator);
		$operatorlist .= $this->_operator_option('startswith', $operator);
		$operatorlist .= $this->_operator_option('endswith', $operator);
		$operatorlist .= '</select> ';

		//v‰‰rtus
		$valuetext = '<input type="text" class="search" name="search_value['. $rownum .']" value="'. $value .'" title="" /> ';

		$vastus .= '<div id="search_row_'. $rownum .'">';
		$vastus .= $taglist . $operatorlist . $valuetext;		
		
		if($addnew==true) {
			$vastus .= '<input type="submit" class="search" id="search_box_add_'. $rownum .'" onclick="new Ajax.Updater(\'new_search_row_'. $rownum .'\',\''. site_url('library/addsearchbox/'. ($rownum+1)) .'\',{asynchronous:true, evalScripts:true}); new Effect.Appear(\'new_search_row_'. $rownum .'\'); new Element.remove(\'search_box_add_'. $rownum .'\'); new Element.show(\'search_box_del_'. $rownum .'\'); return false;" style="width:25px;" value="+" />';
			$del_style = 'display:none;';	
		} else {
			$del_style = '';		
		}
		
		$vastus .= '<input type="submit" class="search" id="search_box_del_'. $rownum .'" onclick="new Effect.Fade(\'search_row_'. $rownum .'\'); new Element.remove(\'search_row_'. $rownum .'\'); return false;" style="'. $del_style .'width:25px;" value="-" />';

		
		$vastus .= '</div>';
		$vastus .= '<div id="new_search_row_'. $rownum .'" style="display:none;"></div>';

		return $vastus;

	}



	function _operator_option($value, $selected_value) {
		$selected = ($value==$selected_value) ? ' selected="selected"' : '';
		return '<option value ="'. $value .'"'. $selected .'>'. $this->CI->lang1->str($value) .'</option>';
	}

	function _tagtype_option($value, $selected_value) {
		$selected = ($value==$selected_value) ? ' selected="selected"' : '';
		return '<option value ="'. $value .'"'. $selected .'>'. mb_convert_case($this->CI->lang1->str($value), MB_CASE_TITLE, "UTF-8") .'</option>';
	}


}

?>