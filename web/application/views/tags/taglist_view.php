<div style="width:120px;" class="right_frame_column">
<?php 
	$row_class = 'table_row_odd';
	if(isset($tags)) foreach ($tags as $tag_id => $tag):
		$row_class = ($row_class=='table_row_even') ? 'table_row_odd' : 'table_row_even';
?>
	<div class="table_row_odd" style="font-size:11px" id="tag_<?= $tag_id; ?>">

		<a class="black_a" href="javascript:void(0);" onclick="$$('.table_row_even').each(element.hide);this.setAttribute('class', 'table_row_even'); new Ajax.Updater('tagvalues','<?= site_url('tags/view/'.$tag['name']); ?>'); return false;" ><?= mb_convert_case($this->lang1->str($tag['name']), MB_CASE_TITLE, "UTF-8"); ?></a>

	</div>
<?php endforeach; ?>

</div>
<div id="tagvalues">XXX</div>

Business Objects Crystal Decisions Applications 
