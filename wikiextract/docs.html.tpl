<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
	<title>Pilvit - Polluting the websphere - Documentation</title>
    <link href='http://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css' />
    <link rel="stylesheet" type="text/css" href="/css/pilvi-style.css" />
	<link rel="shortcut icon" href="/favicon.ico" />
</head>
<body>
<div id="top">
	<div id="topinner">
		<div id="logo">
			<img src="/media/pilvi-handwritten.png" alt="Pilvi" class="logo" />
			<p class="title">polluting the websphere</p>
		</div>
		<div id="menuright">
			<ul id="menu">
				<li class="normal"><a href="/code">CODE</a></li>
				<li class="selected"><a href="/docs">DOCS</a></li>
				<li class="normal"><a href="/about">ABOUT</a></li>
				<li class="empty emptynormal"></li>
			</ul>
		</div>
	</div>
	<div style="clear: both;"></div>
</div>

<div id="fixedoverlay"></div>

<div id="main">
<div class="contentblock">

%s

</div>
</div>

<div id="bottominner" style="margin-top: 30px;">
	<div class="bottomcontacts normal"><a href="mailto:giulio@pilv.it">
		<p class="left normal">E-mail:<br />giulio@pilv.it</p>
		<p class="right"><img src="/media/logo-mail.png" alt="Mail logo" /></p>
	</a></div>
	<div class="bottomcontacts normal"><a href="skype://dullgiulio">
		<p class="left normal">Skype:<br />dullgiulio</p>
		<p class="right"><img src="/media/logo-skype.png" alt="Skype logo" /></p>
	</a></div>
	<div class="bottomcontacts normal"><a href="http://twitter.com/dullboy" target="_blank">
		<p class="left normal">Twitter:<br />twitter.com/dullboy</p>
		<p class="right"><img src="/media/logo-twitter.png" alt="Twitter logo" /></p>
	</a></div>
</div>
<div id="bottom"></div>

<script src="/js/jquery.min.js" type="text/javascript"></script>
<script src="/js/jquery.ui.core.min.js" type="text/javascript"></script>
<script src="/js/jquery.effects.core.min.js" type="text/javascript"></script>
<script src="/js/pilvi-animations.js" type="text/javascript"></script>
<script type="text/javascript">
(function($) {
	$(document).ready(function() {
		$('head').append($('<link>').attr({
			type: 'text/css',
			rel: 'stylesheet',
			href: '/css/pygments/tango.css'
		}));
	});
})(jQuery);
</script>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-1679441-23']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

</body>
</html>
