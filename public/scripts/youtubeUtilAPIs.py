#!/usr/bin/python

import gdata.youtube
import gdata.youtube.service
import sys
import getopt

yt_service = gdata.youtube.service.YouTubeService()

# The YouTube API does not currently support HTTPS/SSL access.
yt_service.ssl = False

def usage():
    print 'py [-t <comma separated title and description>] [-u <video_id>] [-s <video_id>] [-d <video_id>]'
    
def getPostURLAndToken(title, description):
    yt_service.developer_key = 'xxxxxxx' 
    yt_service.client_id = 'xxxxxxx' 
    
    # A complete client login request
    yt_service.email = 'xxxxxxx'
    yt_service.password = 'xxxxxxxx'
    yt_service.source = 'xxxxxxxxxx'
    yt_service.ProgrammaticLogin()

    # create media group as usual
    my_media_group = gdata.media.Group(
      title=gdata.media.Title(text=title),
      description=gdata.media.Description(description_type='plain',
                                          text=description),
      keywords=gdata.media.Keywords(text='travel, entertainment'),
      category=[gdata.media.Category(
          text='Travel',
          scheme='http://gdata.youtube.com/schemas/2007/categories.cat',
          label='Travel')],
      player=None
    )
    
    # create video entry as usual
    video_entry = gdata.youtube.YouTubeVideoEntry(media=my_media_group)    
    # upload meta data only
    response = yt_service.GetFormUploadToken(video_entry)
    return response

# parse response tuple and use the variables to build a form (see next code snippet)
#post_url = response[0]
#youtube_token = response[1]

#print post_url
#print youtube_token
def getVideoEntry(videoID):
    return yt_service.GetYouTubeVideoEntry(video_id=videoID)

def getUploadStatus(videoID):
    entry = getVideoEntry(videoID)
    upload_status = yt_service.CheckUploadStatus(entry)
    return upload_status

def deleteVideoEntry(videoID):
    entry = getVideoEntry(videoID)
    response = yt_service.DeleteVideoEntry(entry)
    if response:
        return True
    else:
        return False

def getVideoURL(videoID):
    entry = getVideoEntry(videoID)
    return entry.media.player.url

#videoID = 'J-g2pE95JD0'
#print getUploadStatus(videoID)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:u:s:d:", ["help"])
    except getopt.GetoptError:           
            usage()                          
            sys.exit(2)
            
    for opt, arg in opts:
        if opt in ("-h", "--help"):      
            usage()                                      
        elif opt == '-t':                
            arr = arg.split(',')
            resp = getPostURLAndToken(arr[0], arr[1])
            print resp[0]+'::'+resp[1]        
        elif opt == '-u': 
             print getVideoURL(arg)
        elif opt == '-s':
            print getUploadStatus(arg)
        elif opt == '-d':
            print deleteVideoEntry(arg)

if __name__ == "__main__":
    main()
