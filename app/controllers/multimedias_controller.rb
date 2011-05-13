#
#
#Copyright (c) 2011 Prabhat Gupta(prabhatgupta.webs.com | golygon.com)
#
#This script may be used for non-commercial purposes only. For any
#commercial purposes, please contact the author at prabhat@golygon.com
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.
#

class MultimediasController < ApplicationController
   
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
