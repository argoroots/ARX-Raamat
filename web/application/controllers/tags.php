<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Tags extends Controller {

	function Tags() {
		parent::Controller();
//		$this->output->enable_profiler(TRUE);

		$this->load->model('tags_model');

	}

	function index() {

		$this->session->protect('library');

		$tags = $this->tags_model->find(null, false);

		if(isset($tags['data'])) $view['tags'] = $tags['data'];

		$view['page_title'] = $this->lang1->str('tags');
		$view['page_footer'] = $this->lang1->str('foundnrows', $tags['row_count']);
		$view['content'] = $this->load->view('tags/taglist_view', $view, True);
		$view['menu'] = $this->session->get_menu('tags');
		$this->load->view('main', $view);

	}


	function view($tagtype = null) {

		$this->session->protect('library');

		$tags = $this->tags_model->find($tagtype, true);

		if(isset($tags['data'])) {
			$firstrow = reset($tags['data']);
			$view['page_title'] = ucfirst($this->lang1->str($firstrow['name']));
			$view['tags'] = $tags['data'];
		}

		$view['page_footer'] = $this->lang1->str('foundnrows', $firstrow['values_count']);
//		$view['content'] = $this->load->view('tags/tag_view', $view, True);
		$view['menu'] = $this->session->get_menu('tags');
		$this->load->view('tags/tag_view', $view);

	}

}

?>
