const str = "barfoofoobarthefoobarman";
const wordz = ["bar","foo","the"];

const str2="barfoothefoobarman";
const wordz2=words = ["foo","bar"];

function findSubstring(s, words) {
    indexArr=[]
    t=(words.length*words[0].length)
    // find all the variations of words concatenations
    newwords=[]
    newwords.push(words.join(''))
    for(var i=1; i<=words.length-1; i++){
        end=words.slice(i).join('');
        beginning=words.slice(0, i).join('');
        newwords.push(end+beginning);
        
    } 
    // use the variations to search the original string

    for(var k=0; k<=s.length-1; k++){
        for (var l=0; l<=newwords.length-1; l++){
            if (s.substring(k,k+t)==newwords[l]){
            indexArr.push(k);
            console.log(indexArr);  
            }
        }
    }
    return indexArr;
};

console.log(findSubstring(str,wordz))
console.log(findSubstring(str2,wordz2))