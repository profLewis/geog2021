# generate a random id

import uuid
div_id = 'i' + str(uuid.uuid4())

html = """<div id="%s" class="map-canvas"/>""" % (div_id)

js = """
<script type="text/Javascript">
  (function(){
    var mapOptions = {
        zoom: 12,
        center: new google.maps.LatLng(51.4412425,-0.2885993)
      };

    var map = new google.maps.Map(document.getElementById('%s'),
          mapOptions);
  })();  
</script>
""" % (div_id)


