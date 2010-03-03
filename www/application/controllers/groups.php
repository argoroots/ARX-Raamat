<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Groups extends Controller {

	function Groups() {
		parent::Controller();
		//$this->output->enable_profiler(TRUE);

		$this->load->model('Library_model');
	}


	function index() {

		$this->session->protect('admin');

		$view['page_title'] = $this->lang1->str('groups');
		$view['menu'] = $this->session->get_menu('groups');

//		$view['content'] = $this->load->view('login/loginform', $view, True);

		$this->load->view('main', $view);

	}

}

?>