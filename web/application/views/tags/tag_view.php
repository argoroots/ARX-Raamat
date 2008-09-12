<div style="width:200px; left:121px" class="right_frame_column">

<?php if(isset($tags)) foreach ($tags as $tag_id => $tag): ?>

<?php 
	$row_class = 'table_row_odd';
	if(isset($tag['values'])) foreach ($tag['values'] as $tagvalue => $tagvalue_count):
		$row_class = ($row_class=='table_row_even') ? 'table_row_odd' : 'table_row_even';
?>
	<div class="<?= $row_class ?>">
		<a class="black_a" href="<?= site_url('tags/view/'); ?>"><?= $tagvalue ?></a>
	</div>
<?php endforeach; ?>

<?php endforeach; ?>

</div>
<div id="tagvalues">XXX</div>
