<?php  if (!defined('BASEPATH')) exit('No direct script access allowed');

class Users extends Controller {

	function Users() {
		parent::Controller();
		//$this->output->enable_profiler(TRUE);
	}


	function index() {

		$this->session->protect('users');

		$view['page_title'] = $this->lang1->str('users');
		$view['menu'] = $this->session->get_menu('users');

		$this->load->view('main', $view);

	}


	function login() {

		if(isset($_POST['login_username']) && isset($_POST['login_password']) && isset($_POST['login_submit']) && isset($_POST['redirect_url'])) { //kui loginform submititi siis logime siisse
		
			if($this->session->login($_POST['login_username'], $_POST['login_password'])==True) { //login õnnestus
				$this->lang1->set_language($this->session->language);
				redirect($_POST['redirect_url']);
				exit();
			} else {
				$view['page_error'] = $this->lang1->str('invalidlogin');
				$view['login_username'] = $_POST['login_username'];
				$view['redirect_url'] = $_POST['redirect_url'];
				$view['login_username'] = $_POST['login_username'];				
			}
			
		} else { //pole formi submitind - kuvame formi
		
			if($this->session->data('redirect_url')) {
				$view['redirect_url'] = $this->session->data('redirect_url');
			} else {
				$view['redirect_url'] = '';
			}
			
		}

		$view['disable_adsense'] = true;			
		$view['page_title'] = $this->lang1->str('login');
		$view['menu'] = $this->session->get_menu();

		$this->load->view('main', $view);

	}


	function logout() {
		$this->session->logout();
		$this->lang1->set_language($this->session->language);
		redirect('');
	}


	function preferences() {
		$view['page_title'] = $this->lang1->str('login');
		$view['menu'] = $this->session->get_menu('preferences');

		$this->load->view('main', $view);
	}
	
	function language($language) {
		
		$url = site_url();
		if(isset($_SERVER['HTTP_REFERER'])) $url = $_SERVER['HTTP_REFERER'];
		
		switch ($language) {
			case 'eng':
				$this->lang1->set_language('eng');
			   break;
			case 'rus':
				$this->lang1->set_language('rus');
			   break;
			default:
				$this->lang1->set_language('est');
		}
		
		header("location:". $url);
		
	}


}

?>