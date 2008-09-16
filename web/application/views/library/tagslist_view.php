<div id="c1" style="padding:0px;overflow-y:hidden; overflow-x:auto; position:absolute;top:0px;bottom:0px;left:0px;right:0px;">
	<div id="c1in" class="right_frame_column">

<?php 
	$row_class = 'row_odd';
	if(isset($tags)) foreach ($tags as $tag_id => $tag):
		//$row_class = ($row_class=='row_even') ? 'row_odd' : 'row_even';
		$onclick = str_replace(array("\r\n", "\r", "\n", "\t"), ' ', "
Effect.Appear('spinner');
$('c2').hide();
new Ajax.Updater('c2','". site_url('library/list_tagvalues/'. $tag_id) ."', {evalScripts:true});
$$('#c1in a.row_selected').invoke('removeClassName', 'row_selected');
$('tag_". $tag_id ."').addClassName('row_selected');
Effect.Fade('spinner');
return false;
		");
?>
		<a id="tag_<?= $tag_id; ?>" class="<?= $row_class; ?>" href="javascript:void(0);" onclick="<?= $onclick; ?>" ><?= mb_convert_case($this->lang1->str($tag['name']), MB_CASE_TITLE, "UTF-8"); ?></a>
<?php endforeach; ?>

	</div>
	<div id="c2"></div>
	<img id="spinner" style="display:none;margin:20px;float:right;" src="/images/spinner.gif">
</div>
