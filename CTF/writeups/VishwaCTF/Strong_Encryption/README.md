# VishwaCTF 2022

## Strong Encryption

**Challenge**

This is our one of the most strong encryption algorithm. Try to decrypt the flag by tracing how it is encrypted.


**Solution**

For this challenge we were given the following code:

```php
 <?php

    // Decrypt -> 576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982452f12f4712f4c769a75b33cb995fa169056168939a8b0b28eafe0d724f18dc4a7

    $flag="";

    function encrypt($str,$enKey){

        $strHex='';
        $Key='';
        $rKey=69;
        $tmpKey='';

        for($i=0;$i<strlen($enKey);$i++){
            $Key.=ord($enKey[$i])+$rKey;
            $tmpKey.=chr(ord($enKey[$i])+$rKey);
        }    

        $rKeyHex=dechex($rKey);

        $enKeyHash = hash('sha256',$tmpKey);

        for ($i=0,$j=0; $i < strlen($str); $i++,$j++){
            if($j==strlen($Key)){
                $j=0;
            }
            $strHex .= dechex(ord($str[$i])+$Key[$j]);
        }
        $encTxt = $strHex.$rKeyHex.$enKeyHash;
        return $encTxt;
    }

    $encTxt = encrypt($flag, "VishwaCTF");

    echo $encTxt;

?> 
```
After a preliminary analysis of the code, we can see that the string to be decrypted consists of three parts:

```php
$encTxt = $strHex.$rKeyHex.$enKeyHash;
```
After dividing the ciphertext into three parts, we get the following values:  

strHex:    576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982  
rKeyHex:   45  
enKeyHash: 2f12f4712f4c769a75b33cb995fa169056168939a8b0b28eafe0d724f18dc4a7 

Then we can see, that enKeyHash is not really needed - it is not used for the encryption of the message. The only thing we need to decrypt the ciphertext is
'Key', which can be easly recovered because we know the enKey - "VishwaCTF", and we see that the Key is created by adding 69 to the ord value of every letter
of the enKey.

To get the flag I wrote this simple script in Python:

```python
enKey = "VishwaCTF"
Key = ''
for character in enKey:
    Key += str(ord(character)+69)
Key += Key
strHex = '576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982'
strHex_divided = [strHex[i:i+2] for i in range(0, len(strHex), 2)]
#  $strHex .= dechex(ord($str[$i])+$Key[$j]);
flag = ''
for i in range(len(strHex_divided)):
    flag += chr(int(strHex_divided[i], 16)-int(Key[i]))
print(flag)
```
```
VishwaCTF{y0u_h4v3_4n_0p_m1nd}
```
