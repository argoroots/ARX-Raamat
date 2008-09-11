<div style="
	border-right-width: 1px;
	border-right-color: #404040;
	border-right-style: solid;
	padding:0px;
	margin:0px;

	position: absolute;
	display: block;
	min-width: 160px;
	right: 0px;
	left: 0px;
	top: 0px;
	bottom: 0px;

	overflow:auto;
">
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
