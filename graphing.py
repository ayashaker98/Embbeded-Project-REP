{\rtf1\ansi\ansicpg1252\cocoartf1671
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 Helvetica-Bold;\f2\fswiss\fcharset0 Helvetica-Oblique;
}
{\colortbl;\red255\green255\blue255;\red8\green8\blue8;\red0\green51\blue179;\red0\green128\blue128;
\red23\green80\blue235;\red140\green140\blue140;\red0\green0\blue128;\red102\green0\blue153;\red0\green55\blue166;
\red6\green125\blue23;\red128\green128\blue128;}
{\*\expandedcolortbl;;\csgenericrgb\c3137\c3137\c3137;\csgenericrgb\c0\c20000\c70196;\csgenericrgb\c0\c50196\c50196;
\csgenericrgb\c9020\c31373\c92157;\csgenericrgb\c54902\c54902\c54902;\csgenericrgb\c0\c0\c50196;\csgenericrgb\c40000\c0\c60000;\csgenericrgb\c0\c21569\c65098;
\csgenericrgb\c2353\c49020\c9020;\csgenericrgb\c50196\c50196\c50196;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs20 \cf2 \uc0\u8232 \cf3 import \cf2 matplotlib.pyplot \cf3 as \cf2 plt\uc0\u8232 \cf3 import \cf2 matplotlib\uc0\u8232 \cf3 from \cf2 matplotlib.animation \cf3 import \cf2 FuncAnimation\uc0\u8232 \cf3 import \cf2 serial\uc0\u8232 \cf3 from \cf2 itertools \cf3 import \cf2 count\uc0\u8232 matplotlib.use(
\f1\b \cf4 "TkAgg"
\f0\b0 \cf2 )\uc0\u8232 x_len = \cf5 50         
\f2\i \cf6 # Number of points to display\uc0\u8232 
\f0\i0 \cf2 y_range = [\cf5 0\cf2 , \cf5 4096\cf2 ]  
\f2\i \cf6 # Range of possible Y values to display\uc0\u8232 
\f0\i0 \cf2 N = 
\f1\b \cf4 "BPM"\uc0\u8232 
\f0\b0 \cf2 fig = plt.figure()\uc0\u8232 ax = fig.add_subplot(\cf5 1\cf2 , \cf5 1\cf2 , \cf5 1\cf2 )\uc0\u8232 xs = \cf7 list\cf2 (\cf7 range\cf2 (\cf5 0\cf2 , \cf5 50\cf2 ))\uc0\u8232 ys = [\cf5 0\cf2 ] * x_len\uc0\u8232 ax.set_ylim(y_range)\u8232 line2, = ax.plot(xs, ys)\u8232 index = count()\u8232 r = \cf7 input\cf2 (
\f1\b \cf4 "Enter Command:"
\f0\b0 \cf2 )\uc0\u8232 COM = \cf7 input\cf2 (
\f1\b \cf4 "Enter Com port: "
\f0\b0 \cf2 )\uc0\u8232 br = \cf7 input\cf2 (
\f1\b \cf4 "Enter BaudRate: "
\f0\b0 \cf2 )\uc0\u8232 ser = serial.Serial(COM,\cf8 baudrate\cf2 =br,\cf8 timeout \cf2 = \cf5 1\cf2 )\uc0\u8232 samplingrate = \cf7 input\cf2 (
\f1\b \cf4 "Enter Sampling Rate:"
\f0\b0 \cf2 )\uc0\u8232 r2 = samplingrate\u8232 samplingrate = samplingrate + 
\f1\b \cf4 "
\f0\b0 \cf9 \\r
\f1\b \cf4 "\uc0\u8232 
\f0\b0 \cf2 ser.write(samplingrate.encode())\uc0\u8232 \cf3 def \cf0 graph\cf2 (sample):\uc0\u8232     l = []\u8232     flag = \cf5 0\uc0\u8232     \cf2 sample = \cf7 int\cf2 (\cf7 int\cf2 (sample) * \cf5 0.20\cf2 )\uc0\u8232     \cf3 for \cf2 i \cf3 in \cf7 range\cf2 (sample):\uc0\u8232         line = ser.readline().decode(
\f1\b \cf4 'utf-8'
\f0\b0 \cf2 )\uc0\u8232         line = line.strip(
\f1\b \cf4 "
\f0\b0 \cf9 \\n
\f1\b \cf4 "
\f0\b0 \cf2 )\uc0\u8232         line = line.strip(
\f1\b \cf4 "
\f0\b0 \cf9 \\r
\f1\b \cf4 "
\f0\b0 \cf2 )\uc0\u8232         \cf3 if \cf2 (line.find(
\f1\b \cf4 "BPM"
\f0\b0 \cf2 ) != -\cf5 1\cf2 ):\uc0\u8232             flag = \cf5 1\uc0\u8232             \cf7 print\cf2 (line)\uc0\u8232         \cf3 elif \cf2 line != \cf10 b''\cf2 :\uc0\u8232             line = line[\cf5 0\cf2 :\cf5 4\cf2 ]\uc0\u8232             \cf3 if \cf2 ((\cf7 len\cf2 (line) > \cf5 0\cf2 ) \cf3 and \cf2 (\cf7 len\cf2 (line) < \cf5 5\cf2 ) \cf3 and \cf2 (line.find(
\f1\b \cf4 '
\f0\b0 \cf9 \\r
\f1\b \cf4 '
\f0\b0 \cf2 ) == -\cf5 1\cf2 )):\uc0\u8232                 \cf7 print\cf2 (line)\uc0\u8232                 line = \cf7 float\cf2 (line)\uc0\u8232                 l.append(line)\u8232     \cf3 return \cf2 l, flag\uc0\u8232 \cf3 def \cf0 animate\cf2 (\cf11 i\cf2 ,ys,sample):\uc0\u8232     l2,flag2 = graph(sample)\u8232     \cf3 if\cf2 (flag2 == \cf5 1\cf2 ):\uc0\u8232         ani.event_source.stop()\u8232     ys.extend(l2)\u8232     ys = ys[-x_len:]\u8232     line2.set_ydata(ys)\u8232     xs.append(\cf7 next\cf2 (index))\uc0\u8232     \cf3 return \cf2 line2,\uc0\u8232 ani = FuncAnimation(fig,\u8232     animate,\u8232     \cf8 fargs\cf2 =(ys,r2),\uc0\u8232     \cf8 interval\cf2 =\cf5 50\cf2 ,\uc0\u8232     \cf8 blit\cf2 =\cf3 True\cf2 )\uc0\u8232 plt.tight_layout()\u8232 plt.show()\
}