<h2>Search operators</h2>

<p class="text">
Search supports the following operators:
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">+</span><br />
A leading plus sign indicates that this word must be present in each result that is returned.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">-</span><br />
A leading minus sign indicates that this word must not be present in any of the results that are returned.<br />
<br />
Note: The - operator acts only to exclude results that are otherwise matched by other search terms. Thus, a search that contains only terms preceded by - returns an empty result. It does not return “all results except those containing any of the excluded terms.”
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">(no operator)</span><br />
By default (when neither + nor - is specified) the word is optional, but the results that contain it are rated higher. This mimics the behavior of MATCH() ... AGAINST() without the IN BOOLEAN MODE modifier.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">&gt; &lt;</span><br />
These two operators are used to change a word's contribution to the relevance value that is assigned to a result. The &gt; operator increases the contribution and the &lt; operator decreases it. See the example following this list.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">( )</span><br />
Parentheses group words into subexpressions. Parenthesized groups can be nested.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">~</span><br />
A leading tilde acts as a negation operator, causing the word's contribution to the result's relevance to be negative. This is useful for marking “noise” words. A result containing such a word is rated lower than others, but is not excluded altogether, as it would be with the - operator.
</p>
<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">*</span><br />
The asterisk serves as the truncation (or wildcard) operator. Unlike the other operators, it should be appended to the word to be affected. Words match if they begin with the word preceding the * operator.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">"</span><br />
A phrase that is enclosed within double quote (“"”) characters matches only results that contain the phrase literally, as it was typed.
</p>


<h2>Search examples</h2>
<p class="text">
The following examples demonstrate some search strings that use boolean full-text operators:
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">apple banana</span><br />
Find results that contain at least one of the two words.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">+apple +juice</span><br />
Find results that contain both words.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">+apple macintosh</span><br />
Find results that contain the word “apple”, but rank results higher if they also contain “macintosh”.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">+apple -macintosh</span><br />
Find results that contain the word “apple” but not “macintosh”.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">+apple ~macintosh</span><br />
Find results that contain the word “apple”, but if the result also contains the word “macintosh”, rate it lower than if result does not. This is “softer” than a search for '+apple -macintosh', for which the presence of “macintosh” causes the result not to be returned at all.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">+apple +(&gt;turnover &lt;strudel)</span><br />
Find results that contain the words “apple” and “turnover”, or “apple” and “strudel” (in any order), but rank “apple turnover” higher than “apple strudel”.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">apple*</span><br />
Find results that contain words such as “apple”, “apples”, “applesauce”, or “applet”.
</p>

<p class="text">
<span style="color:#30455b;font-family: 'Courier New', Courier, Monaco, monospace;">"some words"</span><br />
Find results that contain the exact phrase “some words” (for example, results that contain “some words of wisdom” but not “some noise words”). Note that the “"” characters that enclose the phrase are operator characters that delimit the phrase. They are not the quotes that enclose the search string itself.
</p>
<p class="text">
</p>
