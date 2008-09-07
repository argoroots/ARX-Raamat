<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

	<head profile="http://gmpg.org/xfn/11">
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />

		<title>ARX-Raamat<?php if(isset($page_title)) echo ' : '. $page_title; ?></title>

		<link rel="stylesheet" type="text/css" media="screen" href="<?= site_url('css/screen.css') ?>" />

		<script src="<?= site_url('javascripts/scriptaculous/prototype.js') ?>" type="text/javascript" charset="utf-8"></script>
		<script src="<?= site_url('javascripts/scriptaculous/scriptaculous.js') ?>" type="text/javascript" charset="utf-8"></script>
		<script src="<?= site_url('javascripts/search.js') ?>" type="text/javascript" charset="utf-8"></script>

	</head>	
	<body>

	<div id="header">
		<p id="caption">ARX-Raamat</p>
		<form id="quicksearch" action="<?= site_url('library/submit_search'); ?>" method="post">
			<fieldset>
				<input type="text" id="quicksearch_field" name="quicksearch_field" value="<?php if(isset($quicksearch)) echo $quicksearch; ?>" style="width:200px;" title="<?= $this->lang1->str('search'); ?>" />
			</fieldset>
		</form>
	</div>

	<div id="left_frame">
	
<?php foreach($menu as $key1 => $value1): ?>

		<p class="menu_caption"><?= $key1; ?></p>
			<ul class="menu">

<?php foreach ($value1 as $key2 => $value2): ?>
		<li <?= ($value2['current'])?'class="menu_current"':''; ?>><a href="<?= site_url($value2['url']); ?>"><?= $key2; ?></a></li>
<?php endforeach;?>

			</ul>

<?php endforeach;?>

	
		<div id="left_bottom" <?php if(!isset($login_username)) echo 'style="display:none;"'; ?>>

<?php if($this->session->is_guest==true) { /* Kasutaja on külaline */ ?>
			<form action="https://test.arx.ee/users/login" method="post" style="width: 200px;">
				<fieldset>
					<label for="login_username"><?= $this->lang1->str('username') ?>:</label><br />
					<input type="text" class="login" id="login_username" name="login_username" tabindex="1" value="<?php if(isset($login_username)) echo $login_username; ?>" title="" /><br />
					<label for="login_password"><?= $this->lang1->str('password') ?>:</label><br />
					<input type="password" class="login" id="login_password" name="login_password" tabindex="2" value="" title="" /><br />
					<input type="hidden" id="redirect_url" name="redirect_url" value="<?php if(isset($this->session->redirect_url)) echo $this->session->redirect_url ?>" />
					<input type="submit" id="login_submit" value="OK" name="login_submit" tabindex="3" />
				</fieldset>
			</form>
<?php } ?>
		</div>
	
	</div>


		<div id="right_frame">

		<?php if(isset($tabs)) echo $tabs; ?>

		<?php if(isset($page_filter)) echo '<div id="filter">'. $this->arxui->searchbox($page_filter) .'</div>'; ?>

		<?php if(isset($page_error)) echo '<div id="error"><strong>'. mb_convert_case($this->lang1->str('error'), MB_CASE_UPPER, "UTF-8") .'!</strong><br />'. $page_error .'</div>'; ?>

		<?php if(1==2) { ?>
			<div id="adsense_top">
				<script type="text/javascript"><!--
					google_ad_client = "pub-0063426870039172";
					google_ad_slot = "3796941706";
					google_ad_width = 728;
					google_ad_height = 90;
					//-->
				</script>
				<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"> </script>			

			</div>
		<?php } ?>

		<?php if(isset($content)) echo $content; ?>

		</div>
		<div id="footer">
						<?php if($this->session->is_guest==true) { 
							echo $this->arxui->footer_button(array('javascript:void(0);" onclick="Effect.toggle(\'left_bottom\',\'blind\',{duration:0.3})'=>$this->lang1->str('login')), 'float:left;');
						} else { 
							echo $this->arxui->footer_button(array(site_url('users/logout') => $this->lang1->str('logout')), 'float:left;');
						} ?>
			<?= $this->arxui->footer_button(array('http://validator.w3.org/check?uri=referer' => 'W3C'), 'float:right;'); ?>
			<?php if($this->session->is_guest==true) echo $this->arxui->footer_button(array(site_url('users/language/est')=>'eesti',site_url('users/language/eng')=>'english',site_url('users/language/rus')=>'русский'), 'float:right;') ?>

			<div id="footer_text"><?php if(isset($page_footer)) echo $page_footer; ?></div>
		</div>

		<script type="text/javascript">
			var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
			document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
		</script>
		<script type="text/javascript">
			var pageTracker = _gat._getTracker("UA-260765-7");
			pageTracker._trackPageview();
		</script>

	</body>
</html>