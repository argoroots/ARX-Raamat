<div id="col1" style="overflow-y:hidden; overflow-x:auto;">
	<div id="tagtypes" class="right_frame_column" style="width:120px">

<?php 
	$row_class = 'table_row_odd';
	if(isset($tags)) foreach ($tags as $tag_id => $tag):
		$row_class = ($row_class=='table_row_even') ? 'table_row_odd' : 'table_row_even';
		$onclick = "
Effect.Appear('spinner');
new Ajax.Updater('col2','". site_url('library/tag/'.$tag['id']) ."');
$$('#tagtypes a.column_row').invoke('removeClassName', 'table_row_selected');
$('tag_". $tag_id ."').addClassName('table_row_selected');
Effect.Fade('spinner');
return false;
		";
?>

		<a id="tag_<?= $tag_id; ?>" class="black_a column_row <?= $row_class; ?>" href="javascript:void(0);" onclick="<?= $onclick; ?>" ><?= mb_convert_case($this->lang1->str($tag['name']), MB_CASE_TITLE, "UTF-8"); ?></a>

<?php endforeach; ?>

	</div>
	<div id="col2"></div>
	<img id="spinner" style="display:none;right:20px;top:20px;position:absolute;" src="/images/spinner.gif">
</div>