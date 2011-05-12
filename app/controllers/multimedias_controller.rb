class MultimediasController < ApplicationController
  # Require authentication only for edit and delete operation
   
  # GET /multimedias/new
  # GET /multimedias/new.xml
  def new
  end

  def uploadToken
    cmd = Rails.root.to_s + '/public/scripts/youtubeUtilAPIs.py'
    title = "Test Video"
    description = "Test Video description"
    resp = `#{cmd} -t "#{title},#{description}"`
    resp = resp.split('::')
    response = (resp.length == 2) ? {:uploadUrl => resp[0], :token => resp[1]} : ""
    respond_to do |format|
      format.js {render :js => response.to_json}
    end
  end
end
