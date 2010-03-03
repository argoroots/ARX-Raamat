<?php if(strpos($_SERVER['HTTP_USER_AGENT'], 'MSIE 5')!=false OR strpos($_SERVER['HTTP_USER_AGENT'], 'MSIE 6')!=false) { ?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<title>Not Supported Browser</title>
		<style type="text/css">
			body {
				margin: 50px;
				background: black;
				color: white;
				font-family: "Lucida Grande", "Sans Serif", Arial;
			}
			a:link, a:visited, a:active {
				color: white;
				text-decoration: none;
			}
			a:hover {
				text-decoration: underline;
			}
		</style>
		<script type="text/javascript">
			var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
			document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
		</script>
		<script type="text/javascript">
			var pageTracker = _gat._getTracker("UA-260765-7");
			pageTracker._initData();
			pageTracker._trackPageview();
		</script>
	</head>
	<body>
	<center>
		<img src="/images/sad_mac.png" /><br />
		<strong>Sorry, but Your browser is not compatible with this site!</strong><br /><br />
		<small>
			We support the following browsers:<br />
			<a target="_blank" id="Safari" href="http://www.apple.com/safari/">Safari 3 or later</a><br />
			<a target="_blank" id="Firefox" href="http://www.mozilla.com/firefox/">Firefox 2 or later</a><br />
			<a target="_blank" id="IE" href="http://www.microsoft.com/ie/">Internet Explorer 7 or later</a>
		</small>
	<center>
	</body>
</html>

<?php exit; } ?>