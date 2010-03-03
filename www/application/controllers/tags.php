<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Tags extends Controller {

	function Tags() {
		parent::Controller();
//		$this->output->enable_profiler(TRUE);

		$this->load->model('tags_model');

	}

	function index() {

		$this->session->protect('library');

		$view['tags'] = $this->tags_model->get_tags();

		$view['page_title'] = $this->lang1->str('tags');
		$view['content'] = $this->load->view('tags/taglist_view', $view, True);
		$view['menu'] = $this->session->get_menu('tags');
		$this->load->view('main', $view);

	}


	function view($tagtype = null) {

		$this->session->protect('library');

		$view['tagvalues'] = $this->tags_model->get_tagvalues($tagtype);
		$this->load->view('tags/tagvauelist_view', $view);

	}

}

?>
