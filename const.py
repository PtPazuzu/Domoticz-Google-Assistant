# -*- coding: utf-8 -*-
                    
"""Constants for Google Assistant."""
VERSION = '1.5.2'
PUBLIC_URL = 'https://[YOUR REVERSE PROXY URL]'
CONFIGFILE = 'config.yaml'
LOGFILE = 'dzga.log'
KEYFILE = 'smart-home-key.json'

HOMEGRAPH_URL = "https://homegraph.googleapis.com/"
HOMEGRAPH_SCOPE = "https://www.googleapis.com/auth/homegraph"
HOMEGRAPH_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
REQUEST_SYNC_BASE_URL = HOMEGRAPH_URL + "v1/devices:requestSync"
REPORT_STATE_BASE_URL = HOMEGRAPH_URL + "v1/devices:reportStateAndNotification"

SESSION_TIMEOUT = 3600
AUTH_CODE_TIMEOUT = 600

DOMOTICZ_GET_ALL_DEVICES_URL = '/json.htm?type=devices&plan='
DOMOTICZ_GET_ONE_DEVICE_URL = '/json.htm?type=devices&rid='
DOMOTICZ_GET_SCENES_URL = '/json.htm?type=scenes'
DOMOTICZ_GET_SETTINGS_URL = '/json.htm?type=settings'
DOMOTICZ_GET_CAMERAS_URL = '/json.htm?type=cameras'

#https://developers.google.com/actions/smarthome/guides/
PREFIX_TYPES = 'action.devices.types.'
TYPE_AC_UNIT = PREFIX_TYPES + 'AC_UNIT'
TYPE_BLINDS = PREFIX_TYPES + 'BLINDS'
TYPE_CAMERA = PREFIX_TYPES + 'CAMERA'
TYPE_COFFEE = PREFIX_TYPES + 'COFFEE_MAKER'
TYPE_DISHWASHER = PREFIX_TYPES + 'DISHWASHER'
TYPE_DOOR = PREFIX_TYPES + 'DOOR'
TYPE_DRYER = PREFIX_TYPES + 'DRYER'
TYPE_FAN = PREFIX_TYPES + 'FAN'
TYPE_GATE = PREFIX_TYPES + 'GATE'
TYPE_HEATER = PREFIX_TYPES + 'HEATER'
TYPE_LIGHT = PREFIX_TYPES + 'LIGHT'
TYPE_LOCK = PREFIX_TYPES + 'LOCK'
TYPE_OUTLET = PREFIX_TYPES + 'OUTLET'
TYPE_SCENE = PREFIX_TYPES + 'SCENE'
TYPE_SCREEN = PREFIX_TYPES + 'SCREEN'
TYPE_SECURITY = PREFIX_TYPES + 'SECURITYSYSTEM'
TYPE_SENSOR = PREFIX_TYPES + 'SENSOR'
TYPE_SPEAKER = PREFIX_TYPES + 'SPEAKER'
TYPE_SPRINKLER = PREFIX_TYPES + 'SPRINKLER'
TYPE_SWITCH = PREFIX_TYPES + 'SWITCH'
TYPE_THERMOSTAT = PREFIX_TYPES + 'THERMOSTAT'
TYPE_MEDIA = PREFIX_TYPES + 'TV'
TYPE_VACUUM = PREFIX_TYPES + 'VACUUM'
TYPE_WATERHEATER = PREFIX_TYPES + 'WATERHEATER'
TYPE_WASHER = PREFIX_TYPES + 'WASHER'
TYPE_WINDOW = PREFIX_TYPES + 'WINDOW'

# Error codes used for SmartHomeError class
# https://developers.google.com/actions/smarthome/create-app#error_responses
ERR_DEVICE_OFFLINE = "deviceOffline"
ERR_DEVICE_NOT_FOUND = "deviceNotFound"
ERR_VALUE_OUT_OF_RANGE = "valueOutOfRange"
ERR_NOT_SUPPORTED = "notSupported"
ERR_PROTOCOL_ERROR = 'protocolError'
ERR_UNKNOWN_ERROR = 'unknownError'
ERR_FUNCTION_NOT_SUPPORTED = 'functionNotSupported'
ERR_CHALLENGE_NEEDED = 'challengeNeeded'
ERR_WRONG_PIN = 'pinIncorrect'
ERR_ALREADY_IN_STATE = 'alreadyInState'

groupDOMAIN = 'Group'
sceneDOMAIN = 'Scene'
lightDOMAIN = 'Light'
switchDOMAIN = 'Switch'
outletDOMAIN = 'Outlet'
blindsDOMAIN = 'Blinds'
screenDOMAIN = 'Screen'
climateDOMAIN = 'Thermostat'
tempDOMAIN = 'Temp'
lockDOMAIN = 'DoorLock'
invlockDOMAIN = 'DoorLockInverted'
colorDOMAIN = 'ColorSwitch'
mediaDOMAIN = 'Media'
securityDOMAIN = 'Security'
pushDOMAIN = 'Push'
speakerDOMAIN = 'Speaker'
cameraDOMAIN = 'Camera'
sensorDOMAIN = 'Sensor'
doorDOMAIN = 'DoorSensor'
selectorDOMAIN = 'Selector'
fanDOMAIN = 'Fan'

ATTRS_BRIGHTNESS = 1
ATTRS_THERMSTATSETPOINT = 1
ATTRS_COLOR = 2
ATTRS_COLOR_TEMP = 3
ATTRS_PERCENTAGE = 1

DOMOTICZ_TO_GOOGLE_TYPES = {
    groupDOMAIN: TYPE_SWITCH,
    sceneDOMAIN: TYPE_SCENE,
    lightDOMAIN: TYPE_LIGHT,
    switchDOMAIN: TYPE_SWITCH,
    outletDOMAIN: TYPE_OUTLET,
    blindsDOMAIN: TYPE_BLINDS,
    screenDOMAIN: TYPE_SCREEN,
    climateDOMAIN: TYPE_THERMOSTAT,
    tempDOMAIN: TYPE_THERMOSTAT,
    lockDOMAIN: TYPE_LOCK,
    invlockDOMAIN: TYPE_LOCK,
    colorDOMAIN: TYPE_LIGHT,
    mediaDOMAIN: TYPE_MEDIA,
    securityDOMAIN: TYPE_SECURITY,
    pushDOMAIN: TYPE_SWITCH,
    speakerDOMAIN: TYPE_SPEAKER,
    cameraDOMAIN: TYPE_CAMERA,
    sensorDOMAIN: TYPE_SENSOR,
    doorDOMAIN: TYPE_DOOR,
    selectorDOMAIN: TYPE_SWITCH,
    fanDOMAIN: TYPE_FAN,
}

TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <title>Domoticz Google Assistant v""" + VERSION + """</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    {meta}
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Material Design for Bootstrap fonts and icons -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons">
    <!-- Material Design for Bootstrap CSS -->
    <link rel="stylesheet" href="https://unpkg.com/bootstrap-material-design@4.1.1/dist/css/bootstrap-material-design.min.css" integrity="sha384-wXznGJNEXNG1NFsbm0ugrLFMQPWswR3lds2VeinahP8N0zJw9VWSopbjv2x7WCvX" crossorigin="anonymous">
    <!-- Codemirror CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/codemirror.css" />  
  </head>
  <body>
    <!-- Modal -->
    <div class="modal fade" id="messageModal" tabindex="-1" role="dialog" aria-labelledby="modalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalLabel">Security Risk</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body" id="message">
            Please change the default username and password and restart server!
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <a class="navbar-brand" href="/settings">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Google_Assistant_logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
        Domoticz Google Assistant</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="nav nav-tabs bg-primary">
      <li class="nav-item" data-toggle="tooltip" data-placement="bottom" title="Home">
        <a data-toggle="tab" class="nav-link active" href="#home"><i class="material-icons">home</i></a>
      </li>
      <li class="nav-item" data-toggle="tooltip" data-placement="bottom" title="Devices">
        <a data-toggle="tab" class="nav-link" href="#menu1"><i class="material-icons">devices_other</i></a>
      </li>
      <li class="nav-item" data-toggle="tooltip" data-placement="bottom" title="Configuration">
        <a data-toggle="tab" class="nav-link" href="#menu2"><i class="material-icons">settings_ethernet</i></a>
      </li>
      <li class="nav-item" data-toggle="tooltip" data-placement="bottom" title="Setup Actions on Google">
        <a data-toggle="tab" class="nav-link" href="#menu3"><i class="material-icons">perm_device_information</i></a>
      </li>
      <li class="nav-item" data-toggle="tooltip" data-placement="bottom" title="Help">
        <a data-toggle="tab" class="nav-link" href="#menu4"><i class="material-icons">help_outline</i></a>
      </li>
      <li class="nav-item" data-toggle="tooltip" data-placement="bottom" title="Log">
        <a data-toggle="tab" class="nav-link" href="#menu5"><i class="material-icons">notes</i></a>
      </li>
    </ul>
    </div>
    </nav>
    <!-- Container -->
    <div class="container">
    <div class="tab-content">
        <!-- Start page -->
        <div id="home" class="tab-pane fade show active" role="tabpanel">    
            <div class="row">
              <div class="col-8">
                <p class="lead"><br>This project is based on Pawcio's script at <a href="https://www.domoticz.com/forum/viewtopic.php?f=69&amp;t=27244">domoticz forum</a></p>
                <p class="lead">Domoticz-Google-Assistant delivers:<br />
                <ul>
                    <li>The oauth authorization and smarthome endpoint for the google assistant</li>
                    <li>Two-factor authentication pin for domoticz protected devices (limited language support)</li>
                    <li>Acknowledgement with Yes or No. (limited language support)</li>
                    <li>Arm Disarm Securitypanel (limited language support)</li>
                    <li>On/Off, Brightness, Thermostat, Color Settings, speaker volume, Lock/Unlock, Scene and Open/Close</li>
                    <li>Stream surveillance camera to chromecast</li>
                    <li>Toggle selector devices</li>
                    <li>Ngrok, instantly create a public HTTPS URL. Don't have to open any port on router and do not require a reverse proxy.</li>
                </ul>
                </p>
                <p class="lead">Please feel free to modify, extend and improve it</p>
                <p class="lead text-info">Before you can use dzga. Setup Action on Google and configure settings in configuration.</p>
                <p class="lead"><a href="https://github.com/DewGew/Domoticz-Google-Assistant">&bull; Dzga on Github</a> <a href="https://github.com/DewGew/Domoticz-Google-Assistant/issues">&bull; Report issues</a></p>
              </div>
              <div class="col-4">
                <p>
                <form action="/settings" method="post">
                    <button class="btn btn-raised btn-primary" name="restart" value="restart"><i class="material-icons" style="vertical-align: middle;">replay</i> Restart Server</button>
                    <button class="btn btn-raised btn-primary" name="sync" value="sync"><i class="material-icons" style="vertical-align: middle;">sync</i> Sync Devices</button>
                </form>
                </p>
                <small class="text-muted">
                    <p>Quick start<p>
                    Visit the Actions on Google console at <a href="http://console.actions.google.com">http://console.actions.google.com</a>.<br>Under Develop section, replace the fulfillment URL in Actions with:<br>
                    <kbd>{public_url}/smarthome</kbd><br><br>
                    In Account linking, set the Authorization URL to:<br>
                    <kbd>{public_url}/oauth</kbd><br><br>
                    Then set the Token URL to:<br>
                    <kbd>{public_url}/token</kbd><br><br>
                    Finally press <kbd>SAVE</kbd> and then <kbd>TEST</kbd> button<br>
              </small>
              </div>
            </div>
            <div class="row">
              <div class="col">
                <i class="material-icons" style="vertical-align: middle;">timelapse</i><small class="text-muted"> Sytem Uptime:<br>{uptime}</small>
              </div>
              <div class="col">
                <small class="text-muted">DZGA Version:<br>V""" + VERSION + """</small><br>
                <small class="text-muted" id="updates"></small>
              </div>
              <div class="col" id="buttonUpdate"></div>
              <div class="col-4">
                <small class="text-muted">Encourage the development, please use the button below.</small>
                <center><form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
                <input type="hidden" name="cmd" value="_s-xclick" />
                <input type="hidden" name="hosted_button_id" value="7D7ZWKMDLXA4J" />
                <input type="image" src="https://www.paypalobjects.com/en_US/SE/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
                <img alt="" border="0" src="https://www.paypal.com/en_SE/i/scr/pixel.gif" width="1" height="1" />
                </form></center>
              </div>
            </div>
        </div>
        <div id="menu1" class="tab-pane fade" role="tabpanel">
            <br>
            <h5>Device list</h5>
            <small class="text-muted">List of devices the server recived from domoticz. Room and Nicknames is added from configuration. <b>Click on Header to sort asc or desc</b><br><b>NOTE:</b> If you don't see any device check your connection to domoticz.</small>
            <table class="table" id="deviceTable">
              <thead>
                <tr>
                  <th scope="col" onclick="sortIdxTable(0)">Idx</th>
                  <th scope="col" onclick="sortTable(0)">Name <small><i>(Nicknames)</i></small></th>
                  <th scope="col" onclick="sortTable(1)">Type</th>
                  <th scope="col" onclick="sortTable(2)">State</th>
                  <th scope="col" onclick="sortTable(3)">Room</th>
                </tr>
              </thead>
              <tbody id="deviceList_idx" ></tbody>
            </table>
        </div>
        <div id="menu2" class="tab-pane fade" role="tabpanel">
            <br>
            <h5>Configuration</h5>
            <textarea id="code" style="width: 100%;">{code}</textarea>
            <br>
            <div class="row">
              <div class="col">
              <form action="/settings" method="post">
                <button class="btn btn-raised btn-primary" name="save" id="save"><i class="material-icons" style="vertical-align: middle;">save</i> Save</button>
                <button class="btn btn-raised btn-primary" name="backup" value="backup"><i class="material-icons" style="vertical-align: middle;">save_alt</i> Backup Config</button>
                <button class="btn btn-raised btn-primary" name="restart" value="restart"><i class="material-icons" style="vertical-align: middle;">replay</i> Restart Server</button>
                </form>
                <p class="text-muted">Restart server to activate your changes</p>
              </div>
            </div>
        </div>
        <div id="menu3" class="tab-pane fade" role="tabpanel">
            <br>
            <h5>Setup Actions on Google Console Instructions</h5>
            <ul>
            <li><p>Use the <a href="https://console.actions.google.com/">Actions on Google Console</a> to add a new project with a name of your choosing and click     - Create Project.</p>

            <ul>
            <li>Click Home Control, then click Smart Home.</li>
            <li>On the top menu click Develop, then on the left navigation menu click on Invocation.</li>
            <li>Add your App's name. Click Save.</li>
            <li>Click 'Save'.</li>
            </ul></li><br>
            
            <li><p>Add Credentials</p>
            <ul>
            <li>Navigate to the <a href="https://console.cloud.google.com/apis/credentials">Google Cloud Console API & Service page</a> for your project id.</li>
            <li>Click 'Create credentials'</li>
            <li>Click 'OAuth client ID'</li>
            <li>Choose 'other'</li>
            <li>Add name e.g. 'SmartHomeClientID'</li>
            <li>Copy the client ID shown and insert it in <code>clientID</code> in config.yaml</li>
            <li>Copy the client secret shown and insert it in <code>clientSecret</code> in config.yaml</li>
            </ul></li><br>
            
            <li><p>Add Request Sync and Report State (Optional but recomended)</p>
            <p>The Request Sync feature allows a cloud integration to send a request to the Home Graph to send a new SYNC request. The Report State feature allows a cloud integration to proactively provide the current state of devices to the Home Graph without a QUERY request. These are done securely through JWT (JSON web tokens).</p>

            <ul>
            <li>Navigate to the <a href="https://console.cloud.google.com/apis/library">Google Cloud Console API Manager</a> for your project id.</li>
            <li>Enable the <a href="https://console.cloud.google.com/apis/api/homegraph.googleapis.com/overview">HomeGraph API</a></li>
            <li>Navigate to the <a href="https://console.cloud.google.com/apis/credentials">Google Cloud Console API & Services page</a></li>
            <li>Select <b>Create Credentials</b> and create a <b>Service account key</b></li>
            <ul>
            <li>Create a new Service account</li>
            <li>Use the role Service Account > Service Account Token Creator</li>
            </ul>
            <li>Create the account and download a JSON file. Save this in Domoticz-Google-Assisstant folder as <code>smart-home-key.json</code>.</li>
            </ul></li><br>
            
            <li><p>Navigate back to the <a href="https://console.actions.google.com/">Actions on Google Console</a>.</p>
            <ul>
            <li>On the top menu click Develop, then on the left navigation menu click on Actions.
            Enter the URL for fulfillment, e.g. <code>{public_url}/smarthome</code>, click Done.</li>
            <li>On the left navigation menu under Account Linking.</li>
            <li>Under Client Information, enter the client ID and secret from earlier.</li>
            <li>Change Authorization URL to <code>{public_url}/oauth</code>.</li>
            <li>Change Token URL to <code>{public_url}/token</code>.</li>
            <li>Do NOT check 'Google to transmit clientID and secret via HTTP basic auth header'.</li>
            <li>Click 'Save' at the top right corner, then click 'Test' to generate a new draft version of the Test App.</li>
            </ul></li>
            </ul>
        </div>
        <div id="menu4" class="tab-pane fade" role="tabpanel">
            <br>
            <h5 id="top">Help</h5>
            <p>
            <a href="#C1">Configuration Settings</a><br>
            <a href="#C2">Device Settings</a><br>
            <a href="#C3">Stream camera to chromecast</a><br>
            <a href="#C4">Other</a><br>
            </p>
            <h5 id="C1">Configuration Settings</h5>
            
            <p><code><b>port_settings:</b> 3030</code><br><small class="text-muted">Set the local port. Default is 3030</small></p>
            <p><code><b>loglevel:</b> 'Info'</code><br><small class="text-muted">Set log level <code>Debug</code>, <code>Info</code> or <code>Error</code>. Default is <code>Info</code></small></br> 
            <code><b>logtofile:</b> false</code><br><small class="text-muted">Enable or disable write log to file. Set logtofile to <code>false</code> logs will not show in the LOG tab. Set logtofile to <code>'Overwrite'</code> or <code>true</code> Log file will be overwritten when dzga server restarts. Set logtofile to <code>'Append'</code> Logs will append to logfile if dzga server restarts.</small><br>
            <code><b>pathToLogFile:</b> '/tmp'</code><br><small class="text-muted">Path to log file. If pathToLogFile is commented out, removed or set to '', logs will be saved in Domoticz-Google-Assistant folder</small></p>
            <p><code><b>userinterface:</b> true</code><br><small class="text-muted">Enable or disable UI</small></p>
            <p><code><b>CheckForUpates:</b> true</code><br><small class="text-muted">Enable or disable check for updates</small></p>
            <p><code><b>ngrok_tunnel:</b> true</code><br><small class="text-muted">Use Ngrok tunnel true or false. Instantly create a public HTTPS URL.<br>Don't have to open any port on router and do not require a reverse proxy.<br><b>NOTE:</b> When ngrok_tunnel set to True the auth token is required to keep the tunnel alive. Create account at ngrok.com and paste the token in this file.</small>
            </br><code><b>ngrok_auth_:</b> 'auth_token'</code><br><small class="text-muted">If you use the ngrok tunnel option without account the tunnel will be terminated after 5 or 6 hours. Create account at <a href="https://dashboard.ngrok.com/signup">ngrok.com</a> and paste the token.</small></p>
            
            <p><code><b>auth_user:</b> 'admin'</code><br><small class="text-muted">Set the authorization username.</small></br>
            <code><b>auth_pass:</b> 'admin'</code><br><small class="text-muted">Set the authorization password.</small></p>
            
            <p><small class="text-muted">Add correct ipaddress, port, domoticz credientials to connect to domoticz.</small><br>
            <code><b>Domoticz:</code></b><br>
            <code>&nbsp;&nbsp;<b>ip:</b> 'http://192.168.1.100'</code><br>
            <code>&nbsp;&nbsp;<b>port:</b> '8080'</code><br>
            <code>&nbsp;&nbsp;<b>username:</b>'user'</code></br>
            <code>&nbsp;&nbsp;<b>password:</b>'password'</code></br>
            <code>&nbsp;&nbsp;<b>roomplan:</b> '0'</code></br>
            <code>&nbsp;&nbsp;<b>switchProtectionPass:</b> '1234'</code><br>
            <small class="text-muted">Assign a roomplan. <code>'0'</code> is all devices. Set <code>switchProtectionPass:</code> equal to 'Light/Switch Protection' in domoticz settings. Required to be in numbers to work properly. Set this to <code>false</code> if ask for pin function is not needed.</small></p>
            
            <p><code><b>ClientID:</b> 'ADD_YOUR_CLIENT_ID_HERE'</code></br>
            <code><b>ClientSecret:</b> 'ADD_YOUR_CLIENT_SECRET_HERE'</code><br><small class="text-muted">Set the Google credientials.</small><br>
            <code><b>Homegraph_API_Key:</b> 'ADD_YOUR HOMEGRAPH_API_KEY_HERE' # Not required.</code><br><small class="text-muted">Homegraph API key from Google. The Request Sync feature allows a cloud integration to send a request to the Home Graph to send a new SYNC request.</br>** NOTE: This is not needed if you are using Service account (smart-home-key.json).</small><br>
            </p>
            <p><code><b>Low_battery_limit:</b> 9</code><br><small class="text-muted">Set threhold for report low battery.</small></p>
            <p><small class="text-muted">Ligths, switches, media, etc. are using domoticz's "Light/Switch" type. To differentiate them additionaly add image name (e.g. - 'Light').</small><br>
            <code><b>Image_Override:</b><br>
            <b>&nbsp;&nbsp;Switch:</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'Generic'<br>
            &nbsp;&nbsp;<b>Light:</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'Light'<br>
            &nbsp;&nbsp;<b>Media:</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'Media'<br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'TV'<br>
            &nbsp;&nbsp;<b>Outlet:</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'WallSocket'<br>
            &nbsp;&nbsp;<b>Speaker:</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'Speaker'<br>
            &nbsp;&nbsp;<b>Fan:</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'Fan'</code><br>
            <small class="text-muted">Support device types <code>Switch Light Media Outlet Speaker Fan</code>. Its possible to remove those that you don't need.</small></p>
            <p><code><b>Camera_Stream:</b></code><br><small class="text-muted">In domoticz you need to attach a switch to your camera, Add switch idx and camera stream url. <a href="#C3">Read more below</a>.</small><p>
            <p><small class="text-muted">User-friendly name for the arm level in your language.</small><br>
            <code><b>Armhome:</b><br>
            &nbsp;&nbsp;<b>level_synonym:</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'låg säkerhet'<br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'Level 1'<br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'hemmaläge'<br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'SL1'<br>
            &nbsp;&nbsp;<b>lang:</b> 'sv'<br>
            <b>Armaway:</b><br>
            &nbsp;&nbsp;<b>level_synonym:</b><br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'hög säkerhet'<br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'Level 2'<br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'bortaläge'<br>
            &nbsp;&nbsp;&nbsp;&nbsp;- 'SL2'<br>
            &nbsp;&nbsp;<b>lang:</b> 'sv'
            </code></p>
            
            <h5 id="C2">Device Settings</h5>

            <p><small class="text-muted">Nicknames, rooms, ack and report_state can be set in the Domoticz user interface. Simply put the device configuration in the device description, in a section between &lt;voicecontrol&gt; tags like:
            <code></small><br />
            &lt;voicecontrol&gt;<br />
            &nbsp;&nbsp;nicknames = Kitchen Blind One, Left Blind, Blue Blind<br />
            &nbsp;&nbsp;room = Kitchen<br />
            &nbsp;&nbsp;ack = True<br />
            &nbsp;&nbsp;report_state = false<br />
            &lt;/voicecontrol&gt;<br />
            </code>
            <small class="text-muted">Other parts of the description are ignored, so you can still leave other useful descriptions.
            Every variable should be on a separate line.
            If there is no such configuration in the Domoticz device it will still try the config.</small></p>

            <h5 id="C3">Stream camera to chromecast</h5>

            <p><small class="text-muted">Stream security camera to chromecast. Supports hls, dash, smooth streaming, Progressive MP4 urls. More info: https://developers.google.com/actions/smarthome/traits/camerastream#video-formats. You need a to convert your video url to one of above. Try with ffmpeg or with a surveillance software system. Try out http://shinobi.video. <br />
            In domoticz you need to attach a switch to your camera (create a switch then in Settings/Camera, add the switch to the camera)</small></p>
            <p><code><b>Camera_Stream: </b></code><br>
            <code>&nbsp;&nbsp;<b>Enabled:</b> true </code><small class="text-muted"># Enable/disable cast to chromecast</small><br>
            <code>&nbsp;&nbsp;<b>Cameras:</b> </code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;<b>Idx:</b></br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- '123' </code><small class="text-muted"># Idx of camera attached device</small><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;<b>Camera_URL:</b></br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'https://content.jwplatform.com/manifests/yp34SRmf.m3u8' </code><small class="text-muted"># Stream url</small><br>
            </p>
            <p><small class="text-muted">Example convert rtsp to hls or mp4 using ffmpeg:</small><br />
            <code>
            ffmpeg -rtsp_transport tcp -i rtsp://admin:123456@192.168.0.218/live/ch1 \
              -acodec copy \
              -vcodec copy \
              -hls_wrap 40 \
              -flags -global_header \
              /var/www/html/cam/cam.m3u8
            </code><br />
            <code>
            ffmpeg -rtsp_transport tcp -i rtsp://admin:123456@192.168.0.218/live/ch1 \
              -c:a aac \
              -vcodec copy \
              -f mp4 \
              -y \
              -flags -global_header \
              /var/www/html/cam/cam.mp4
            </code>
            </p>
            
            <h5 id="C4">Other</h5>
            
            <h6><small class="text-muted">Connect smart home devices to your Google Home device</h6>
            <ul>
            <li>On your mobile device, open the Google Home app.</li>
            <li>On the Home tab, tap the “Add” quick action .</li>
            <li>Tap Set up a device</li>
            <li>Tap Have something already set up?</li>
            <li>Select your device app e.g: "[test]Your Appname"</li>
            <li>Login with auth credentials from config</li>
            </ul></small>
            
            <h6>Share devices</h6>

            <p><small class="text-muted">If you want to allow other household users to control the devices:<br />
            <ul>
            <li>Go to the settings for the project you created in the <a href="https://console.actions.google.com/">Actions on Google Console</a>.</li>
            <li>Click <code>Test -&gt; Simulator</code>, then click Share icon in the right top corner. Follow the on-screen instruction:</li>
            <li>Add team members:</li>
            <li>Got to <code>Settings -&gt; Permission</code>, click Add, type the new user’s e-mail address and choose <code>Project -&gt; Viewer role</code>.</li>
            <li>Copy and share the link with the new user.</li>
            <li>When the new user opens the link with their own Google account, it will enable your draft test app under their account.</li>
            <li>Have the new user go to their Google Home app to add "[test]Your Appname" to their account. Login with Oauth credentials from config.py</li>
            </ul></small></p>
            
            <h6>Update</h6>

            <p>
            <kbd>bash <(curl -s https://raw.githubusercontent.com/DewGew/dzga-installer/master/install.sh)</kbd><br>
            <small class="text-muted">or</small><br>
            <code>
            cd /home/${{USER}}/Domoticz-Google-Assistant/<br>
            git pull
            </code><br />
            <small class="text-muted">If needed, restart service:</small><br />
            <code>
            sudo systemctl restart dzga.service
            </code><br /></p>
            <p><a href="#top">Goto Top</a></p>
        </div>
        <div id="menu5" class="tab-pane fade" role="tabpanel">
            <br>
            <h5 id="logsheader">Logs</h5>
            <textarea id="logs" rows="20" style="font-size: 10pt; width: 100%;">{logs}</textarea>
            <br>
            <div class="row">
              <div class="col">
              <form action="/settings" method="post">
                <button class="btn btn-raised btn-primary" name="reload" value="reload"><i class="material-icons" style="vertical-align: middle;">sync</i> Reload logs</button>
                <button class="btn btn-raised btn-primary" name="deletelogs" value="deletelogs"><i class="material-icons" style="vertical-align: middle;">delete</i> Remove logs</button>
               </form>
              </div>
            </div>
        </div>
    </div>
    </div>
    
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/popper.js@1.12.6/dist/umd/popper.js" integrity="sha384-fA23ZRQ3G/J53mElWqVJEGJzU0sTs+SvzG8fXVWP+kJQ1lwFAOkcUOysnlKJC33U" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/bootstrap-material-design@4.1.1/dist/js/bootstrap-material-design.js" integrity="sha384-CauSuKpEqAFajSpkdjv3z9t8E7RlpJ1UP0lKM/+NdtSarroVKu069AlsRPKkFBz9" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/codemirror.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/mode/yaml/yaml.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/addon/display/autorefresh.js"></script>
    <script>
    function sortTable(n) {{
      var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
      table = document.getElementById("deviceTable");
      switching = true;
      dir = "asc";
      while (switching) {{
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {{
          shouldSwitch = false;
          x = rows[i].getElementsByTagName("TD")[n];
          y = rows[i + 1].getElementsByTagName("TD")[n];
          if (dir == "asc") {{
            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {{
              shouldSwitch = true;
              break;
            }}
          }} else if (dir == "desc") {{
            if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {{
              shouldSwitch = true;
              break;
            }}
          }}
        }}
        if (shouldSwitch) {{
          rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
          switching = true;
          switchcount ++;
        }} else {{
          if (switchcount == 0 && dir == "asc") {{
            dir = "desc";
            switching = true;
          }}
        }}
      }}
    }}
    function sortIdxTable(n) {{
      var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
      table = document.getElementById("deviceTable");
      switching = true;
      dir = "asc";
      while (switching) {{
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {{
          shouldSwitch = false;
          x = rows[i].getElementsByTagName("TH")[n];
          y = rows[i + 1].getElementsByTagName("TH")[n];
          if (dir == "asc") {{
            if (Number(x.innerHTML) > Number(y.innerHTML)) {{
              shouldSwitch = true;
              break;
            }}
          }} else if (dir == "desc") {{
            if (Number(x.innerHTML) < Number(y.innerHTML)) {{
              shouldSwitch = true;
              break;
            }}
          }}
        }}
        if (shouldSwitch) {{
          rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
          switching = true;
          switchcount ++;
        }} else {{
          if (switchcount == 0 && dir == "asc") {{
            dir = "desc";
            switching = true;
          }}
        }}
      }}
    }}

    $(document).ready(function() {{    
        var config = {conf}
        var updates = {update}
        document.getElementById("logsheader").innerHTML = 'Logs <small class="text-muted">Loglevel: ' + config.loglevel + '</small>';
        if (updates) {{
          document.getElementById("updates").innerHTML = "Updates are Availible.";
          // document.getElementById("modalLabel").innerHTML = "Updates are Availible!";
          // document.getElementById("message").innerHTML = '<p>Updates are Availible. Just press update button to get latest Dzga version.</p><p><center><form action="/settings" method="post"><button class="btn btn-raised btn-primary" name="update" value="update"><i class="material-icons" style="vertical-align: middle;">update</i> Update</button></form></center></p>';
          // $('#messageModal').modal('show')
          $('#buttonUpdate').append('<br><form action="/settings" method="post"><button class="btn btn-raised btn-primary" name="update" value="update"><i class="material-icons" style="vertical-align: middle;">update</i> Update</button></form>');
        }};
        
        $('body').bootstrapMaterialDesign();
        $(function () {{
          $('[data-toggle="tooltip"]').tooltip()
        }});
        
        if (config.auth_user == 'admin' || config.auth_pass == 'admin'){{
            $('#messageModal').modal('show')
        }};
        message = '{message}'
        if (message != '') {{
            document.getElementById("modalLabel").innerHTML = "Information!";
            document.getElementById("message").innerHTML = message;
            $('#messageModal').modal('show')
        }};

        var devicelist = {list}
        
        var x,i, nicknames = "";
        for (i in devicelist){{
            if (devicelist[i][4] == undefined) {{
                devicelist[i][4] = " "
            }}
            if (devicelist[i][5] == undefined) {{
                nicknames = " ";
            }}else{{ nicknames = " <small><i>(" + devicelist[i][5] + ")</i></small>"}}
            x += "<tr><th scope='row'>" + devicelist[i][1] + "</th><td>" + devicelist[i][0] +  nicknames + "</td><td>" + devicelist[i][2] + "</td><td>" + devicelist[i][3] + "</td><td>" + devicelist[i][4] + "</td></tr>";

        }};
        if (typeof x !== "undefined"){{
            $('#deviceList_idx').append(x.replace('undefined',''));
        }}else{{
            document.getElementById("modalLabel").innerHTML = "Check configuration.";
            document.getElementById("message").innerHTML = "Connection to Domoticz refused! Check configuration.";
            $('#messageModal').modal('show')
        }};
            
        var editor = CodeMirror.fromTextArea(document.getElementById("code"), {{
            lineNumbers: true,
            mode: "yaml",
            autoRefresh:true
        }});
        editor.setOption("extraKeys", {{
          Tab: function(cm) {{
            var spaces = Array(cm.getOption("indentUnit") + 1).join(" ");
            cm.replaceSelection(spaces);
          }}
        }});
        editor.on("change", function() {{
            textTosave = editor.getValue();
            document.getElementById("save").value = textTosave;
         }});
         
        document.getElementById("save").value = document.getElementById("code").value
    
    }});</script>    
  </body>
</html>
"""
