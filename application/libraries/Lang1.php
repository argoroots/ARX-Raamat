<?php if(!defined('BASEPATH')) exit('No direct script access allowed');

/*

Keele (tõlke) klass

*/

class Lang1 {

	function Lang1() {

		//CI klassi kasutamine
		$this->CI =& get_instance();
		$this->CI->load->database();

		if(!isset($_SESSION)) session_start();
		if(!isset($_SESSION['lang']['language_id'])) $this->set_language();

	}



//Tagastab tõlgitud stringi
	function str($string, $str1 = null, $str2 = null) {

		if(!isset($_SESSION['lang']['language_id'])) $this->set_language();

		if(isset($_SESSION['lang'][$string])) {
			//string leiti ja tagastame selle
			$vastus = $_SESSION['lang'][$string];
			if(isset($str1)) $vastus = str_replace('@1', $str1, $vastus);
			if(isset($str2)) $vastus = str_replace('@2', $str2, $vastus);
		} else {
			//stringi ei leitud. Lisame baasi ja tagastame key
			$query = $this->CI->db->query('INSERT IGNORE INTO systemstrings SET
				name = LOWER(\''. $string .'\'),
				est = LOWER(\'@'. $string .'\'),
				eng = LOWER(\'@'. $string .'\')
				
			');
			$vastus = $string;
		}

		return $vastus;

	}



// salvestab kasutaja keele array sessiooni
	function set_language($language = 'eng') {

		unset($_SESSION['lang']);

		$query = $this->CI->db->query('
			SELECT
				name,
				'. $language .' AS text
			FROM
				systemstrings
			ORDER BY name
			');

		foreach ($query->result_array() as $row) {
			$_SESSION['lang'][$row['name']] = $row['text'];
		}
		
		$_SESSION['lang']['language_id'] = $language;
		
	}

}

?>