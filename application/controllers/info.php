<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Info extends Controller {

	function Info() {
		parent::Controller();
	}


	function index() {

		$view['menu'] = $this->session->get_menu('');
		$this->load->view('main', $view);

	}

	function help() {

		$view['page_title'] = $this->lang1->str('help');
		$view['menu'] = $this->session->get_menu('help');

		$view['content'] = $this->load->view('info/help_eng', $view, True);

		$this->load->view('main', $view);

	}

	function contact() {

		$view['page_title'] = $this->lang1->str('contact');
		$view['menu'] = $this->session->get_menu('contact');

		$view['content'] = $this->load->view('info/contact', $view, True);

		$this->load->view('main', $view);

	}

}

?>