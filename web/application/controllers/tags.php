<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Tags extends Controller {

	function Tags() {
		parent::Controller();
//		$this->output->enable_profiler(TRUE);

		$this->load->model('tags_model');

	}

	function index() {
		redirect('tags/view/all');
	}


	function view($id = null) {

		$this->session->protect('library');

		if($id=='all') {

		}	elseif (!isnumeric($id)) {
			redirect('tags/view/all');
		} else {
		
		}
		
		$media = $this->media_model->find($filter_array, 1, 50, True, False);

		if(isset($media['data'])) {
			$view['media'] = $media['data'];
			$view['page_footer'] = $this->lang1->str('foundnrows', $media['row_count']);
		}

		$view['page_title'] = $this->lang1->str('catalogue');
		$view['menu'] = $this->session->get_menu('library');
		$view['content'] = $this->load->view('library/media_table_view', $view, True);
		$this->load->view('main', $view);

	}

}

?>