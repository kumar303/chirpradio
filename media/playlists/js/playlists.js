// requires: chirp/chirp.js
//           jquery.autocomplete/jquery.autocomplete.js

$(document).ready(function() {
    
    var default_opt = {
        selectFirst: false,
        minChars: 3,
        delay: 400,
        maxItemsToShow: 15,
        matchContains: true // tells the cache to do substring matches 
                            // (necessary when searching "eno" and the 
                            // result is "Eno, Brian")
    };
    
    $("#id_artist").autocomplete("/djdb/artist/search.txt", 
        $.extend({
            onItemSelect: function(li) {
                var entity_key = li.extra[0];
                $("#id_artist_key").attr("value", entity_key);
            }
        }, default_opt)
    );
    
    $("#id_album").autocomplete("/djdb/album/search.txt", 
        $.extend({
            onItemSelect: function(li) {
                var entity_key = li.extra[0];
                $("#id_album_key").attr("value", entity_key);
            }
        }, default_opt)
    );
    
    $("#id_song").autocomplete("/djdb/track/search.txt", 
        $.extend({
            onItemSelect: function(li) {
                var entity_key = li.extra[0];
                $("#id_song_key").attr("value", entity_key);
            }
        }, default_opt)
    );
    
    // be sure that freeform entry always clears out any 
    // previously auto-completed keys :
    
    $("#id_artist").change(function() {
        $("#id_artist_key").attr("value", "");
    });
    $("#id_album").change(function() {
        $("#id_album_key").attr("value", "");
    });
    $("#id_song").change(function() {
        $("#id_song_key").attr("value", "");
    });
    
});