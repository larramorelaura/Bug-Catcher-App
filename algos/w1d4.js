/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcdddaaa";
  const expected1 = "a4b2cd3a3";
  const expected1b = "a4bbcd3a3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "ccbb";
  const expected4 = "ccbb";
  
  const str5 = "abbbbbbbbbbbbbbbbb"
  const expected5 = "ab17"
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
  // RIOT  Read Input Output Talk
  
function encodeStr(str) {
    if(str.length==1){
        return str;
    }
    if(str.length==0){
        return "\"\"";
    }
    
    var newStr="";
    var count=0;
    for(let i=0; i<str.length-1; i++){
        if (str[i]!=str[i+1]){
            newStr+=str[i];
        }
        else{
            newStr+=str[i];
            while(str[i]==str[i+1]){
                count++;
                i++;
                if(i==str.length-1){
                    count++;
                }
            }
            
            newStr+=count;
            count=0;
        }
    }
    if (newStr.length==str.length){
        return str;
    }
    else{
        return newStr;
    }
}
  
  console.log(encodeStr(str1)) // Expected: a4bbcd3
  console.log(encodeStr(str2)) // Expected: ""
  console.log(encodeStr(str3)) // Expected: a
  console.log(encodeStr(str4)) // Expected: ccbb
  console.log(encodeStr(str5)) // Expected: ab17
  
  const strA = "a3b2c1d3";
  const expectedA = "aaabbcddd";
  
  const strB = "a3b2c12d10";
  const expectedB = "aaabbccccccccccccdddddddddd";
  
  /**
   * Decodes the given string by duplicating each character by the following int
   * amount if there is an int after the character.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str An encoded string with characters that may have an int
   *    after indicating how many times the character occurs.
   * @returns {string} The given str decoded / expanded.
   */
  //helpful built-ins : isNaN() .repeat() parseInt() NaN
  function decodeStr(str) {
    var newString=""
    var counts=0
    var numbers=""
      for (var i=0; i<str.length; i++){
        if (isNaN(str[i])==true){
            newString+=str[i];
            console.log(newString);
        }
        else{
            numbers+=str[i];
            console.log(numbers);
        }
        counts=parseInt(numbers);
        newString+=str[i].repeat([counts]); 
      }
      return newString;
  }
  
  console.log(decodeStr(strA)) // Expected: aaabbcddd
  console.log(decodeStr(strB)) // Expected: aaabbccccccccccccdddddddddd