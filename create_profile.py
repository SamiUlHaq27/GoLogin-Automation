import gologin


def create_profile(token, host:str, port:int, usr:str, pas:str):
    gl = gologin.GoLogin({
        "token":token
    })
    
    recommended = {
  "name": "Auto Profile",
#   "id": "65d6d64c3594c6e54244d6db",
  "notes": "",
  "browserType": "chrome",
  "canBeRunning": True,
  "os": "win",
  "startUrl": "",
  "autoLang": True,
  "googleServicesEnabled": False,
  "isBookmarksSynced": True,
  "lockEnabled": False,
  "debugMode": None,
  "navigator": {
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.110 Safari/537.36",
    "resolution": "1440x900",
    "language": "en-US,en;q=0.8",
    "platform": "Win32",
    "hardwareConcurrency": 8,
    "doNotTrack": False,
    "deviceMemory": 8,
    "maxTouchPoints": 0
  },
  "storage": {
    "local": True,
    "extensions": True,
    "bookmarks": True,
    "history": True,
    "passwords": True,
    "session": True,
    "indexedDb": False,
    "enableExternalExtensions": False
  },
  "proxyEnabled": True,
  "autoProxyServer": "",
  "autoProxyUsername": "",
  "autoProxyPassword": "",
  "proxy": {
    # "id": "65d6d64cdbce984c497f26be",
    "mode": "http",
    "host": host,
    "port": port,
    "autoProxyRegion": "us",
    "torProxyRegion": "us",
    "username": usr,
    "password": pas
  },
  "dns": "",
  "plugins": {
    "enableVulnerable": True,
    "enableFlash": True
  },
  "timezone": {
    "enabled": True,
    "fillBasedOnIp": True,
    "timezone": ""
  },
  "geolocation": {
    "mode": "block",
    "enabled": True,
    "customize": True,
    "fillBasedOnIp": True,
    "latitude": 0,
    "longitude": 0,
    "accuracy": 10,
    "isCustomCoordinates": False
  },
  "audioContext": {
    "mode": "noise",
    "noise": 5.659613929577e-08
  },
  "canvas": {
    "mode": "off",
    "noise": 0.64608144
  },
  "fonts": {
    "enableMasking": True,
    "enableDomRect": True,
    "families": [
      "AIGDT",
      "AMGDT",
      "Arial",
      "Arial Baltic",
      "Arial Black",
      "Arial CE",
      "Arial Greek",
      "Arial Hebrew",
      "Arial Narrow",
      "Arial Rounded MT Bold",
      "Arial Unicode MS",
      "Cambria Math",
      "Candara",
      "Comic Sans MS",
      "Consolas",
      "Constantia",
      "Corbel",
      "Courier",
      "Courier New",
      "Courier New Cyr",
      "Courier New Greek",
      "David",
      "David Libre",
      "DejaVu Sans Condensed",
      "DejaVu Sans Mono",
      "DejaVu Serif",
      "DejaVu Serif Condensed",
      "Ebrima",
      "Frank Ruehl",
      "Frank Ruehl Libre",
      "Frank Ruehl Libre Black",
      "Frank Ruehl Libre Light",
      "Franklin Gothic Book",
      "Franklin Gothic Demi",
      "Franklin Gothic Demi Cond",
      "Franklin Gothic Heavy",
      "Franklin Gothic Medium",
      "Franklin Gothic Medium Cond",
      "Gabriola",
      "Gadugi",
      "Georgia",
      "Gill Sans",
      "Gill Sans MT",
      "Gill Sans MT Condensed",
      "Gill Sans MT Ext Condensed Bold",
      "Gill Sans Ultra Bold",
      "Gill Sans Ultra Bold Condensed",
      "Impact",
      "KacstBook",
      "KacstLetter",
      "KacstNaskh",
      "KacstTitlel",
      "Leelawadee",
      "Liberation Mono",
      "Liberation Sans",
      "Liberation Sans Narrow",
      "Liberation Serif",
      "Lucida Bright",
      "Lucida Calligraphy",
      "Lucida Console",
      "Lucida Sans Unicode",
      "MS Gothic",
      "MS Mincho",
      "MS Outlook",
      "MS PGothic",
      "MS PMincho",
      "MS Reference Sans Serif",
      "MS Reference Specialty",
      "MS Sans Serif",
      "MS Serif",
      "MS UI Gothic",
      "MV Boli",
      "Malgun Gothic",
      "Microsoft Himalaya",
      "Microsoft JhengHei",
      "Microsoft JhengHei UI",
      "Microsoft New Tai Lue",
      "Microsoft PhagsPa",
      "Microsoft Sans Serif",
      "Microsoft Tai Le",
      "Microsoft Uighur",
      "Microsoft YaHei",
      "Microsoft YaHei UI",
      "Microsoft Yi Baiti",
      "MingLiU",
      "MingLiU_HKSCS",
      "MingLiU_HKSCS-ExtB",
      "Miriam",
      "Miriam Fixed",
      "Mongolian Baiti",
      "NSimSun",
      "Nirmala UI",
      "Noto Mono",
      "Noto Sans",
      "Noto Sans Arabic UI",
      "Noto Sans CJK HK",
      "Noto Sans CJK JP",
      "Noto Sans CJK KR",
      "Noto Sans CJK SC",
      "Noto Sans CJK TC",
      "Noto Sans Lisu",
      "Noto Sans Mono CJK HK",
      "Noto Sans Mono CJK JP",
      "Noto Sans Mono CJK KR",
      "Noto Sans Mono CJK SC",
      "Noto Serif CJK JP",
      "Noto Serif CJK KR",
      "Noto Serif CJK SC",
      "Noto Serif CJK TC",
      "Noto Serif Hebrew",
      "Noto Serif Italic",
      "Noto Serif Lao",
      "OpenSymbol",
      "Oswald",
      "PMingLiU",
      "PMingLiU-ExtB",
      "Palatino",
      "Palatino Linotype",
      "Roboto",
      "Roboto Black",
      "Roboto Light",
      "Roboto Medium",
      "Roboto Thin",
      "Segoe Print",
      "Segoe Script",
      "Segoe UI",
      "Segoe UI Light",
      "Segoe UI Semibold",
      "Segoe UI Semilight",
      "Segoe UI Symbol",
      "SimSun",
      "Sylfaen",
      "Symbol",
      "Tahoma",
      "Times New Roman",
      "Times New Roman Baltic",
      "Times New Roman CE",
      "Times New Roman Greek",
      "Times New Roman TUR",
      "Trebuchet MS",
      "Verdana",
      "Webdings",
      "Wingdings",
      "Wingdings 2",
      "Wingdings 3",
      "Yu Gothic",
      "Yu Gothic UI",
      "Zapf Dingbats"
    ]
  },
  "mediaDevices": {
    "enableMasking": True,
    "uid": "498117f609bd4083a6c624a671c9697ab8c8a6273d0f4b558c793d4b89",
    "videoInputs": 1,
    "audioInputs": 1,
    "audioOutputs": 1
  },
  "webRTC": {
    "enable": False,
    "isEmptyIceList": True,
    "mode": "disabled",
    "enabled": True,
    "customize": True,
    "localIpMasking": False,
    "fillBasedOnIp": True,
    "publicIp": "",
    "localIps": []
  },
  "webGL": {
    "mode": "off",
    "getClientRectsNoise": 8.12866,
    "noise": 8.964
  },
  "clientRects": {
    "mode": "off",
    "noise": 8.12866
  },
  "webGLMetadata": {
    "mode": "mask",
    "vendor": "Google Inc. (Intel)",
    "renderer": "ANGLE (Intel, Intel(R) UHD Graphics 620 (0x00003EA0) Direct3D11 vs_5_0 ps_5_0, D3D11)"
  },
  "webglParams": {
    "glCanvas": "webgl2",
    "supportedFunctions": [
      {
        "name": "beginQuery",
        "supported": True
      },
      {
        "name": "beginTransformFeedback",
        "supported": True
      },
      {
        "name": "bindBufferBase",
        "supported": True
      },
      {
        "name": "bindBufferRange",
        "supported": True
      },
      {
        "name": "bindSampler",
        "supported": True
      },
      {
        "name": "bindTransformFeedback",
        "supported": True
      },
      {
        "name": "bindVertexArray",
        "supported": True
      },
      {
        "name": "blitFramebuffer",
        "supported": True
      },
      {
        "name": "clearBufferfi",
        "supported": True
      },
      {
        "name": "clearBufferfv",
        "supported": True
      },
      {
        "name": "clearBufferiv",
        "supported": True
      },
      {
        "name": "clearBufferuiv",
        "supported": True
      },
      {
        "name": "clientWaitSync",
        "supported": True
      },
      {
        "name": "compressedTexImage3D",
        "supported": True
      },
      {
        "name": "compressedTexSubImage3D",
        "supported": True
      },
      {
        "name": "copyBufferSubData",
        "supported": True
      },
      {
        "name": "copyTexSubImage3D",
        "supported": True
      },
      {
        "name": "createQuery",
        "supported": True
      },
      {
        "name": "createSampler",
        "supported": True
      },
      {
        "name": "createTransformFeedback",
        "supported": True
      },
      {
        "name": "createVertexArray",
        "supported": True
      },
      {
        "name": "deleteQuery",
        "supported": True
      },
      {
        "name": "deleteSampler",
        "supported": True
      },
      {
        "name": "deleteSync",
        "supported": True
      },
      {
        "name": "deleteTransformFeedback",
        "supported": True
      },
      {
        "name": "deleteVertexArray",
        "supported": True
      },
      {
        "name": "drawArraysInstanced",
        "supported": True
      },
      {
        "name": "drawBuffers",
        "supported": True
      },
      {
        "name": "drawElementsInstanced",
        "supported": True
      },
      {
        "name": "drawRangeElements",
        "supported": True
      },
      {
        "name": "endQuery",
        "supported": True
      },
      {
        "name": "endTransformFeedback",
        "supported": True
      },
      {
        "name": "fenceSync",
        "supported": True
      },
      {
        "name": "framebufferTextureLayer",
        "supported": True
      },
      {
        "name": "getActiveUniformBlockName",
        "supported": True
      },
      {
        "name": "getActiveUniformBlockParameter",
        "supported": True
      },
      {
        "name": "getActiveUniforms",
        "supported": True
      },
      {
        "name": "getBufferSubData",
        "supported": True
      },
      {
        "name": "getFragDataLocation",
        "supported": True
      },
      {
        "name": "getIndexedParameter",
        "supported": True
      },
      {
        "name": "getInternalformatParameter",
        "supported": True
      },
      {
        "name": "getQuery",
        "supported": True
      },
      {
        "name": "getQueryParameter",
        "supported": True
      },
      {
        "name": "getSamplerParameter",
        "supported": True
      },
      {
        "name": "getSyncParameter",
        "supported": True
      },
      {
        "name": "getTransformFeedbackVarying",
        "supported": True
      },
      {
        "name": "getUniformBlockIndex",
        "supported": True
      },
      {
        "name": "getUniformIndices",
        "supported": True
      },
      {
        "name": "invalidateFramebuffer",
        "supported": True
      },
      {
        "name": "invalidateSubFramebuffer",
        "supported": True
      },
      {
        "name": "isQuery",
        "supported": True
      },
      {
        "name": "isSampler",
        "supported": True
      },
      {
        "name": "isSync",
        "supported": True
      },
      {
        "name": "isTransformFeedback",
        "supported": True
      },
      {
        "name": "isVertexArray",
        "supported": True
      },
      {
        "name": "pauseTransformFeedback",
        "supported": True
      },
      {
        "name": "readBuffer",
        "supported": True
      },
      {
        "name": "renderbufferStorageMultisample",
        "supported": True
      },
      {
        "name": "resumeTransformFeedback",
        "supported": True
      },
      {
        "name": "samplerParameterf",
        "supported": True
      },
      {
        "name": "samplerParameteri",
        "supported": True
      },
      {
        "name": "texImage3D",
        "supported": True
      },
      {
        "name": "texStorage2D",
        "supported": True
      },
      {
        "name": "texStorage3D",
        "supported": True
      },
      {
        "name": "texSubImage3D",
        "supported": True
      },
      {
        "name": "transformFeedbackVaryings",
        "supported": True
      },
      {
        "name": "uniform1ui",
        "supported": True
      },
      {
        "name": "uniform1uiv",
        "supported": True
      },
      {
        "name": "uniform2ui",
        "supported": True
      },
      {
        "name": "uniform2uiv",
        "supported": True
      },
      {
        "name": "uniform3ui",
        "supported": True
      },
      {
        "name": "uniform3uiv",
        "supported": True
      },
      {
        "name": "uniform4ui",
        "supported": True
      },
      {
        "name": "uniform4uiv",
        "supported": True
      },
      {
        "name": "uniformBlockBinding",
        "supported": True
      },
      {
        "name": "uniformMatrix2x3fv",
        "supported": True
      },
      {
        "name": "uniformMatrix2x4fv",
        "supported": True
      },
      {
        "name": "uniformMatrix3x2fv",
        "supported": True
      },
      {
        "name": "uniformMatrix3x4fv",
        "supported": True
      },
      {
        "name": "uniformMatrix4x2fv",
        "supported": True
      },
      {
        "name": "uniformMatrix4x3fv",
        "supported": True
      },
      {
        "name": "vertexAttribDivisor",
        "supported": True
      },
      {
        "name": "vertexAttribI4i",
        "supported": True
      },
      {
        "name": "vertexAttribI4iv",
        "supported": True
      },
      {
        "name": "vertexAttribI4ui",
        "supported": True
      },
      {
        "name": "vertexAttribI4uiv",
        "supported": True
      },
      {
        "name": "vertexAttribIPointer",
        "supported": True
      },
      {
        "name": "waitSync",
        "supported": True
      }
    ],
    "glParamValues": [
      {
        "name": "ALIASED_LINE_WIDTH_RANGE",
        "value": {
          "0": 1,
          "1": 1
        }
      },
      {
        "name": "ALIASED_POINT_SIZE_RANGE",
        "value": {
          "0": 1,
          "1": 1024
        }
      },
      {
        "name": [
          "DEPTH_BITS",
          "STENCIL_BITS"
        ],
        "value": "n/a"
      },
      {
        "name": "MAX_3D_TEXTURE_SIZE",
        "value": 2048
      },
      {
        "name": "MAX_ARRAY_TEXTURE_LAYERS",
        "value": 2048
      },
      {
        "name": "MAX_COLOR_ATTACHMENTS",
        "value": 8
      },
      {
        "name": "MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS",
        "value": 200704
      },
      {
        "name": "MAX_COMBINED_TEXTURE_IMAGE_UNITS",
        "value": 32
      },
      {
        "name": "MAX_COMBINED_UNIFORM_BLOCKS",
        "value": 24
      },
      {
        "name": "MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS",
        "value": 212992
      },
      {
        "name": "MAX_CUBE_MAP_TEXTURE_SIZE",
        "value": 16384
      },
      {
        "name": "MAX_DRAW_BUFFERS",
        "value": 8
      },
      {
        "name": "MAX_FRAGMENT_INPUT_COMPONENTS",
        "value": 120
      },
      {
        "name": "MAX_FRAGMENT_UNIFORM_BLOCKS",
        "value": 12
      },
      {
        "name": "MAX_FRAGMENT_UNIFORM_COMPONENTS",
        "value": 4096
      },
      {
        "name": "MAX_FRAGMENT_UNIFORM_VECTORS",
        "value": 1024
      },
      {
        "name": "MAX_PROGRAM_TEXEL_OFFSET",
        "value": 7
      },
      {
        "name": "MAX_RENDERBUFFER_SIZE",
        "value": 16384
      },
      {
        "name": "MAX_SAMPLES",
        "value": 16
      },
      {
        "name": "MAX_TEXTURE_IMAGE_UNITS",
        "value": 16
      },
      {
        "name": "MAX_TEXTURE_LOD_BIAS",
        "value": 2
      },
      {
        "name": "MAX_TEXTURE_SIZE",
        "value": 16384
      },
      {
        "name": "MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS",
        "value": 120
      },
      {
        "name": "MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS",
        "value": 4
      },
      {
        "name": "MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS",
        "value": 4
      },
      {
        "name": "MAX_UNIFORM_BLOCK_SIZE",
        "value": 65536
      },
      {
        "name": "MAX_UNIFORM_BUFFER_BINDINGS",
        "value": 24
      },
      {
        "name": "MAX_VARYING_COMPONENTS",
        "value": 120
      },
      {
        "name": "MAX_VARYING_VECTORS",
        "value": 30
      },
      {
        "name": "MAX_VERTEX_ATTRIBS",
        "value": 16
      },
      {
        "name": "MAX_VERTEX_OUTPUT_COMPONENTS",
        "value": 120
      },
      {
        "name": "MAX_VERTEX_TEXTURE_IMAGE_UNITS",
        "value": 16
      },
      {
        "name": "MAX_VERTEX_UNIFORM_BLOCKS",
        "value": 12
      },
      {
        "name": "MAX_VERTEX_UNIFORM_COMPONENTS",
        "value": 16384
      },
      {
        "name": "MAX_VERTEX_UNIFORM_VECTORS",
        "value": 4096
      },
      {
        "name": "MAX_VIEWPORT_DIMS",
        "value": {
          "0": 32767,
          "1": 32767
        }
      },
      {
        "name": "MIN_PROGRAM_TEXEL_OFFSET",
        "value": -8
      },
      {
        "name": [
          "RED_BITS",
          "GREEN_BITS",
          "BLUE_BITS",
          "ALPHA_BITS"
        ],
        "value": "n/a"
      },
      {
        "name": "RENDERER",
        "value": "WebKit WebGL"
      },
      {
        "name": "SHADING_LANGUAGE_VERSION",
        "value": "WebGL GLSL ES 3.00 (OpenGL ES GLSL ES 3.0 Chromium)"
      },
      {
        "name": "UNIFORM_BUFFER_OFFSET_ALIGNMENT",
        "value": 256
      },
      {
        "name": "VENDOR",
        "value": "WebKit"
      },
      {
        "name": "VERSION",
        "value": "WebGL 2.0 (OpenGL ES 3.0 Chromium)"
      }
    ],
    "antialiasing": True,
    "textureMaxAnisotropyExt": 16,
    "shaiderPrecisionFormat": "highp/highp",
    "extensions": [
      "EXT_color_buffer_float",
      "EXT_color_buffer_half_float",
      "EXT_disjoint_timer_query_webgl2",
      "EXT_float_blend",
      "EXT_texture_compression_bptc",
      "EXT_texture_compression_rgtc",
      "EXT_texture_filter_anisotropic",
      "EXT_texture_norm16",
      "KHR_parallel_shader_compile",
      "OES_draw_buffers_indexed",
      "OES_texture_float_linear",
      "OVR_multiview2",
      "WEBGL_clip_cull_distance",
      "WEBGL_compressed_texture_s3tc",
      "WEBGL_compressed_texture_s3tc_srgb",
      "WEBGL_debug_renderer_info",
      "WEBGL_debug_shaders",
      "WEBGL_lose_context",
      "WEBGL_multi_draw",
      "WEBGL_provoking_vertex"
    ]
  },
  "extensions": {
    "enabled": True,
    "preloadCustom": True,
    "names": []
  },
  "s3Path": "zero_profile.zip",
  "s3Date": "",
  "devicePixelRatio": 1,
  "owner": "65d6d5c4a51541fc78fcd4b5",
  "checkCookies": False,
  "chromeExtensions": [
    "fjkmabmdepjfammlpliljpnbhleegehm",
    "bppamachkoflopbagkdoflbgfjflfnfl",
    "gchcfdihakkhjgfmokemfeembfokkajj"
  ],
  "userChromeExtensions": [],
  "permissions": {
    "transferProfile": True,
    "transferToMyWorkspace": True,
    "shareProfile": True,
    "manageFolders": True,
    "editProfile": True,
    "deleteProfile": True,
    "cloneProfile": True,
    "exportProfile": True,
    "updateUA": True,
    "addVpnUfoProxy": True,
    "runProfile": True,
    "viewProfile": True,
    "addProfileTag": True,
    "removeProfileTag": True
  }
}
    
    profile_id = gl.create(options=recommended)
    return profile_id
    

    
    

