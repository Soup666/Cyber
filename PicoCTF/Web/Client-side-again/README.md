# Client-side-again

```
Author: Danny
Description

Can you break into this super secure portal? https://jupiter.challenges.picoctf.org/problem/60786/ (link) or http://jupiter.challenges.picoctf.org:60786
```

```php
var original_array=['f49bf}','_again_e','this','Password\x20Verified','Incorrect\x20password','getElementById','value','substring','picoCTF{','not_this'];

(function(arg1,arg2){
	var my_func=function(my_funct_arg){
		while(--my_funct_arg){
			arg1['push'](arg1['shift']());
		}
	};
	my_func(++arg2);
}
(original_array,435));

var my_func_2=function(my_arg1,my_arg2){
	return original_array[my_arg1];
};

function verify(){
	checkpass=document['getElementById']('pass')['value'];
	split=4;
	if(checkpass['substring'](0,8)=='picoCTF{'){
		if(checkpass['substring'](7,9)=='{n'){
			if(checkpass['substring'](8,16)=='not_this'){
				if(checkpass['substring'](3,6)=='oCT'){
					if(checkpass['substring'](24,32)=='f49bf}'){
						if(checkpass['substring'](6,11)=='F{not'){
							if(checkpass['substring'](16,24)=='_again_e'){
								if(checkpass['substring'](12,16)=='this'){
									alert('Password Verified');
								}
							}
						}
					}
				}
			}
		}
	}
	else
	{
		alert(_0x4b5b('9'));
	}
}
```
# Flag: 
`picoCTF{not_this_again_ef49bf}`