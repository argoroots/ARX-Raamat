<?php
	$row_class = 'table_row_odd';
	if(isset($media)) foreach ($media as $media_id => $media_value):
		$row_class = ($row_class=='table_row_even') ? 'table_row_odd' : 'table_row_even';
?>
		
<div class="<?= $row_class ?>">
	<a class="black_a" href="javascript:void(0);" onclick="Effect.toggle('tags_<?= $media_id ?>','blind',{duration:0.3})"><?= $media_value['title'] ?></a>
	<div id="tags_<?= $media_id ?>" style="display:none;"><div>
		<table class="vertical_table" cellspacing="0" cellpadding="0">
		<?php if(isset($media_value['tags'])) foreach ($media_value['tags'] as $tag_id => $tag_value): if(is_array($tag_value)) { ?>
			<tr valign="top">
				<th><?= $this->lang1->str($tag_id) ?>:</th>
				<td>
					<?= $this->arxui->tag_links($tag_id, $tag_value) ?>
				</td>
			</tr>
		<?php } endforeach; ?>
		</table>
	</div></div>
</div>

<?php endforeach; ?>
