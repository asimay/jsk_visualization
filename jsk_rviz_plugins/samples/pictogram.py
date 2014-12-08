#!/usr/bin/env python

import rospy
from jsk_rviz_plugins.msg import Pictogram

rospy.init_node("pictogram_sample")
p = rospy.Publisher("/pictogram", Pictogram)

r = rospy.Rate(5)

pictograms = ["phone",
              "mobile",
              "mouse",
              "address",
              "mail",
              "paper-plane",
              "pencil",
              "feather",
              "attach",
              "inbox",
              "reply",
              "reply-all",
              "forward",
              "user",
              "users",
              "add-user",
              "vcard",
              "export",
              "location",
              "map",
              "compass",
              "direction",
              "hair-cross",
              "share",
              "shareable",
              "heart",
              "heart-empty",
              "star",
              "star-empty",
              "thumbs-up",
              "thumbs-down",
              "chat",
              "comment",
              "quote",
              "home",
              "popup",
              "search",
              "flashlight",
              "print",
              "bell",
              "link",
              "flag",
              "cog",
              "tools",
              "trophy",
              "tag",
              "camera",
              "megaphone",
              "moon",
              "palette",
              "leaf",
              "note",
              "beamed-note",
              "new",
              "graduation-cap",
              "book",
              "newspaper",
              "bag",
              "airplane",
              "lifebuoy",
              "eye",
              "clock",
              "mic",
              "calendar",
              "flash",
              "thunder-cloud",
              "droplet",
              "cd",
              "briefcase",
              "air",
              "hourglass",
              "gauge",
              "language",
              "network",
              "key",
              "battery",
              "bucket",
              "magnet",
              "drive",
              "cup",
              "rocket",
              "brush",
              "suitcase",
              "traffic-cone",
              "globe",
              "keyboard",
              "browser",
              "publish",
              "progress-3",
              "progress-2",
              "progress-1",
              "progress-0",
              "light-down",
              "light-up",
              "adjust",
              "code",
              "monitor",
              "infinity",
              "light-bulb",
              "credit-card",
              "database",
              "voicemail",
              "clipboard",
              "cart",
              "box",
              "ticket",
              "rss",
              "signal",
              "thermometer",
              "water",
              "sweden",
              "line-graph",
              "pie-chart",
              "bar-graph",
              "area-graph",
              "lock",
              "lock-open",
              "logout",
              "login",
              "check",
              "cross",
              "squared-minus",
              "squared-plus",
              "squared-cross",
              "circled-minus",
              "circled-plus",
              "circled-cross",
              "minus",
              "plus",
              "erase",
              "block",
              "info",
              "circled-info",
              "help",
              "circled-help",
              "warning",
              "cycle",
              "cw",
              "ccw",
              "shuffle",
              "back",
              "level-down",
              "retweet",
              "loop",
              "back-in-time",
              "level-up",
              "switch",
              "numbered-list",
              "add-to-list",
              "layout",
              "list",
              "text-doc",
              "text-doc-inverted",
              "doc",
              "docs",
              "landscape-doc",
              "picture",
              "video",
              "music",
              "folder",
              "archive",
              "trash",
              "upload",
              "download",
              "save",
              "install",
              "cloud",
              "upload-cloud",
              "bookmark",
              "bookmarks",
              "open-book",
              "play",
              "paus",
              "record",
              "stop",
              "ff",
              "fb",
              "to-start",
              "to-end",
              "resize-full",
              "resize-small",
              "volume",
              "sound",
              "mute",
              "flow-cascade",
              "flow-branch",
              "flow-tree",
              "flow-line",
              "flow-parallel",
              "left-bold",
              "down-bold",
              "up-bold",
              "right-bold",
              "left",
              "down",
              "up",
              "right",
              "circled-left",
              "circled-down",
              "circled-up",
              "circled-right",
              "triangle-left",
              "triangle-down",
              "triangle-up",
              "triangle-right",
              "chevron-left",
              "chevron-down",
              "chevron-up",
              "chevron-right",
              "chevron-small-left",
              "chevron-small-down",
              "chevron-small-up",
              "chevron-small-right",
              "chevron-thin-left",
              "chevron-thin-down",
              "chevron-thin-up",
              "chevron-thin-right",
              "left-thin",
              "down-thin",
              "up-thin",
              "right-thin",
              "arrow-combo",
              "three-dots",
              "two-dots",
              "dot",
              "cc",
              "cc-by",
              "cc-nc",
              "cc-nc-eu",
              "cc-nc-jp",
              "cc-sa",
              "cc-nd",
              "cc-pd",
              "cc-zero",
              "cc-share",
              "cc-remix",
              "db-logo",
              "db-shape",
              "github",
              "c-github",
              "flickr",
              "c-flickr",
              "vimeo",
              "c-vimeo",
              "twitter",
              "c-twitter",
              "facebook",
              "c-facebook",
              "s-facebook",
              "google+",
              "c-google+",
              "pinterest",
              "c-pinterest",
              "tumblr",
              "c-tumblr",
              "linkedin",
              "c-linkedin",
              "dribbble",
              "c-dribbble",
              "stumbleupon",
              "c-stumbleupon",
              "lastfm",
              "c-lastfm",
              "rdio",
              "c-rdio",
              "spotify",
              "c-spotify",
              "qq",
              "instagram",
              "dropbox",
              "evernote",
              "flattr",
              "skype",
              "c-skype",
              "renren",
              "sina-weibo",
              "paypal",
              "picasa",
              "soundcloud",
              "mixi",
              "behance",
              "google-circles",
              "vk",
              "smashing"]

counter = 0
while not rospy.is_shutdown():
    msg = Pictogram()
    msg.header.frame_id = "/base_link"
    msg.header.stamp = rospy.Time.now()
    msg.pose.position.z = 1.6
    msg.pose.orientation.w = 0.7
    msg.pose.orientation.x = 0
    msg.pose.orientation.y = -0.7
    msg.pose.orientation.z = 0
    msg.size = 0.1
    msg.color.r = 25 / 255.0
    msg.color.g = 255 / 255.0
    msg.color.b = 240 / 255.0
    msg.color.a = 1.0
    msg.character = pictograms[counter]
    p.publish(msg)
    r.sleep()
    counter = counter + 1
    if len(pictograms) == counter:
        counter = 0
