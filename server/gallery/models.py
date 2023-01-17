from django.utils.text import slugify
from django.db import models
from PIL.ExifTags import TAGS
from PIL import Image,TiffImagePlugin
import exifread as ef
# from GPSPhoto import gpsphoto
from geopy.geocoders import Nominatim
# Create your models here.
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images')
    alt = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.JSONField(blank=True, default=dict)
    address = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, blank=True)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at',]
    def save(self, *args, **kwargs):
        
        
        def _convert_to_degress(value):
            """
            Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
            :param value:
            :type value: exifread.utils.Ratio
            :rtype: float
            """
            d = float(value.values[0].num) / float(value.values[0].den)
            m = float(value.values[1].num) / float(value.values[1].den)
            s = float(value.values[2].num) / float(value.values[2].den)

            return d + (m / 60.0) + (s / 3600.0)
        def getGPS(file):
            '''
            returns gps data if present other wise returns empty dictionary
            '''
            tags = ef.process_file(file)
            latitude = tags.get('GPS GPSLatitude')
            latitude_ref = tags.get('GPS GPSLatitudeRef')
            longitude = tags.get('GPS GPSLongitude')
            longitude_ref = tags.get('GPS GPSLongitudeRef')
            if latitude:
                lat_value = _convert_to_degress(latitude)
                if latitude_ref.values != 'N':
                    lat_value = -lat_value
            else:
                return {}
            if longitude:
                lon_value = _convert_to_degress(longitude)
                if longitude_ref.values != 'E':
                    lon_value = -lon_value
            else:
                return {}
            return {'latitude': lat_value, 'longitude': lon_value}
        
        
        if not self.location:
            gps = getGPS(self.image)
            self.location = gps or {}
        # if there is no slug, create one from the alt, if there is no alt, create one from the image name
        if not self.slug:
            if self.alt:
                self.slug = slugify(self.alt)
            else:
                file_name_without_extension = self.image.name.split(".")[0]
                self.slug = slugify(file_name_without_extension)
                
            # if there is a duplicate slug, append a number to the end of it
            if GalleryImage.objects.filter(slug=self.slug).exists():
                i = 1
                while GalleryImage.objects.filter(slug=self.slug + "-" + str(i)).exists():
                    i += 1
                self.slug = self.slug + "-" + str(i)
        if not self.address and self.location:
            geolocator = Nominatim(user_agent="valen")
            address = geolocator.reverse(f"{self.location['latitude']}, {self.location['longitude']}")
            self.address = address.address
        return super().save(*args, **kwargs)