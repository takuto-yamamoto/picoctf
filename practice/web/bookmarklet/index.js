(function () {
  var encryptedFlag = 'àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÒËÉ§©í';
  var key = 'picoctf';
  var decryptedFlag = '';
  for (var i = 0; i < encryptedFlag.length; i++) {
    decryptedFlag += String.fromCharCode(
      (encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256
    );
  }
  alert(decryptedFlag);
})();
