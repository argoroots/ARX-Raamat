<div style="
	border-right-width: 1px;
	border-right-color: #404040;
	border-right-style: solid;
	padding:0px;
	margin:0px;

	display: block;
	position: absolute;
	width: 50%;
	left: 0px;
	top: 0px;
	bottom: 0px;

	overflow:auto;
">

<?php 
	$row_class = 'table_row_odd';
	if(isset($tags)) foreach ($tags as $tag_id => $tag):
		$row_class = ($row_class=='table_row_even') ? 'table_row_odd' : 'table_row_even';
?>
	<div class="<?= $row_class ?>">
		<a class="black_a" href="<?= site_url('tags/view/'.$tag['name']); ?>"><?= ucfirst($this->lang1->str($tag['name'])) ?></a>
	</div>
<?php endforeach; ?>

</div>

