
# Controller Plugin

A plugins to add Joystick and Slider controls to your Synfig animations.


## Demo

!["Demo"](https://i.imgur.com/3S3XhmX.gif "Demo")


## Features

- Easily create Joystick and Slider controls for your animations
- Bind multiple animations to one controller
- Unbind a controller to make changes
- Give custom names for your controller


## Installation

Download the zip file, extract it's content to the plugins folder.


## How to use

The plugin can be used to Joystick controls for you animations.
A joystick is a controller which you can use to interpolate between 5 poses. They must be in order. Normal, Right, Left, Top, Down (NRLTD - Never Run Like The Devil)

Follow the below steps to have Joystick controllers for your animation:
1. You need 5 poses in the order Normal, Right, Left, Top, Down
2. You can create these pose however you like, you must have 5 waypoints for each animated parameter.
3. Rename the group/layer as joystick_name, (ex, joystick_head)
4. Run the plugin
5. You can now see a Joystick controller

## Slider

Sliders are useful to animate between 2 poses. You can create multiple sliders and combine different poses.

Follow the below steps to have Slider controller for you animation:
1. Create any number of poses you want (the plugin will consider the waypoints)
2. Rename the group/layer as slider_name
3. Run the plugin
4. You can see sliders

Slider will interpolate from initial pose which is first waypoint to *n*th waypoint. Now let's suppose your 1st waypoint is on frame 0, and next waypoints are on 3, 5, 7 frames. Then 3 slider's will be created. Which will interpolate from 0-3 pose, 0-5 pose, 0-7 pose.
When the first slider `Slider name 3` is at full value, and other are 0 value then the representation will be of animation at frame 3.
Similar to 5, 7 frame. But the power of slider is that you can combine whatever the value of 3 and 5 frame is.

# FAQ

### When should I use Joystick ?
Use Joystick when you have to interpolate between 5 poses (head animation, faux 3d, complex transitions between multiple poses).

### What is priority for nested Joystick/Slider ?
The innermost Controls are built first and then the parents are built. This also means that the innermost controller will control the elements rather than parent.

### Controls are generated but not working ?
Check the heirarchy of the your Groups, and then find the innermost group which is generating the Control. The innermost Control will control the layer/group's behaviour. It's parent's won't affect it.

### I have found an unexpected behaviour, what should I do ?
Submit an issue, before you submit an issue. Prepare 2 files, the file before running the plugin. After executing the plugin. (If possible, also provide file that is fixed or having expected behaviour). If you can't share your working file, please try to reproduce with simpler shapes.

### When should I use Slider ?
Sliders are useful for interpolating between 2 poses. You can have multiple sliders and combine their values.

### Does this plugin support creating Controls for exported values ?
Currently this doesn't support creating Controls for exported values, but there is a workaround.

Do these steps before running plugin:

1. Bake the exported values (Right click → Bake)
2. Unexport them (Right click → Unexport)

### How is this project related to Joystick and Slider's available for after effects ?
This project isn't directly related to Joysticks and Sliders plugin. This is an independent project, which is inspired from the Joysticks and Sliders.

### What license is this plugin distributed ?
This plugin is published in Public Domain, meaning you can do anything with it for personal and commercial use too.

### I have more questions, what should I do ?
Create a issue here on Github, I am also active on [Synfig Forums](https://forums.synfig.org/).

### I haven't understood how this works, what should I do ?
This FAQ section and documentation is always improving, please open a new issue to ask your questions.
