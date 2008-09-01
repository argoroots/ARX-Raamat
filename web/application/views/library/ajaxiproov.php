
<?php if(isset($media)) foreach ($media as $key => $value): ?>
		<li><?= $value['title']; ?></li>
<?php endforeach; ?>




<br />

<form action="/library/submit_search" method="post">
	<input type="text" name="field" value="" title="" />
	<input type="text" name="search" id="sss" value="" title="" style="width:240px;"/> 
	<br /><input type="submit" id="search_submit" value="<?= $this->lang1->str('login') ?>" name="search_submit" />
</form>


<pre>
<?php /*print_r($media);*/ ?>
</pre>





<div id="quicksearch_field_auto_complete" class="autocomplete"></div>
<img style="display:none;" id="spinner" src="/images/spinner.gif">
<?php //echo $this->ajax->auto_complete_field('quicksearch_field', array('url'=>'/library/ajax_search', 'indicator'=>'spinner')); ?>

<?php //echo $this->ajax->link_to_remote("Login", array('url' => '/library/test', 'update' => 'testbox', 'effect' => 'appear')); ?>
<?php //echo $this->ajax->link_to_function("Hide Ad", "Effect.Unfold('testbox')"); ?>
<?php /*echo $this->ajax->link_to_function("Hide Ad", "Effect.toggle('adsense_top','appear')");*/ ?>
