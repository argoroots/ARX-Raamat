<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Library extends Controller {

	function Library() {
		parent::Controller();
//		$this->output->enable_profiler(TRUE);

		$this->load->model('media_model');
		$this->load->model('search_model');
	}

	function index() {
		redirect('library/search');
	}

//formi poolt submititakse otsing siia ja see suunab urlile edasi
	function submit_search() {

		if(isset($_POST['search_submit'])) { //submititi mitu välja - paneme kokku array ja redirectime otsingu urlile

			$url_array['type'] = $_POST['search_type'];
			foreach($_POST['search_tagtype'] as $key => $value) {
				$url_array['search'][] = array(
					'tagtype'=>$value,
					'operator'=>$_POST['search_operator'][$key],
					'value'=>$_POST['search_value'][$key]
				);
			}
			
			redirect('library/search/'. rawurlencode(serialize($url_array))); 
		} else { //submititi string - redirectime otsingu urlile
			redirect('library/search/'. rawurlencode($_POST['quicksearch_field'])); 
		}

	}

//otsib etteantud stringi järgi
	function search($filter = null, $page = null) {

		$this->session->protect('library');

		$filter_array = @unserialize(rawurldecode($filter)); //proovime lugeda array

		if(!is_numeric($page)) $page = 1;
		$result_per_page = 100;
		
		if(empty($filter_array)) { //ei olnud array - loeme stringina
			$filter = rawurldecode($filter);
			if(mb_strlen($filter, 'utf8') > 3) { //otsingutekst on piisava pikkusega
				$media =  $this->media_model->find($filter, $page, $result_per_page, True, False);	
			} else { //otsingutekst on liig lühike - viga
				if(mb_strlen($filter, 'utf8')>0) $view['page_error'] = $this->lang1->str('tooshortsearchstring');
			}
			$view['quicksearch'] = $filter;
		} else {//oli array - kasutame seda
			$media =  $this->media_model->find($filter_array, $page, $result_per_page, True, False);
			$view['page_filter'] = $filter_array;
		}
		
		if(isset($media['data'])) {
			$view['media'] = $media['data'];
			$view['page_footer'] = $this->lang1->str('foundnrows', $media['row_count']);
		} else {
			//$view['page_error'] = $this->lang1->str('noresults');	
		}

		$view['page_title'] = $this->lang1->str('catalogue');
		$view['menu'] = $this->session->get_menu('library');
		$view['content'] = $this->load->view('library/media_table_view', $view, True);
		$this->load->view('main', $view);

	}

	function ajax_search() {

		$this->session->protect('library', false);

		$list = $this->media_model->title_list($_POST['quicksearch_field'], 10);
		
		if(isset($list)) {
			echo '<ul>';
			foreach($list as $key => $value) {
				echo '<li id="'. $key .'">'. $value .'</li>';
			}
			echo '</ul>';
		} else {
			echo 'Eimiskit';
		
		}
	}
	
	function addsearchbox($rownumber) {

		echo $this->arxui->add_searchbox($rownumber);

	}
	
}

?>