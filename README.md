{\rtf1\ansi\ansicpg1252\cocoartf1671
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 Arial-BoldMT;\f2\fswiss\fcharset0 ArialMT;
\f3\froman\fcharset0 TimesNewRomanPSMT;\f4\froman\fcharset0 TimesNewRomanPS-BoldMT;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs48 \cf0 HEART BEAT MONITOR\
\pard\pardeftab720\ri-340\partightenfactor0

\f1\b\fs24 \cf0 Overview:\

\f2\b0 For my project I\'92ve chosen to implement a simple heart monitor, using the ECG Sensor AD8232, and STM32 Microcontroller. The Electrodes are placed on someone for the ECG to detect the heart beat, and then the output from the ECG Sensor is sent as an analog signal to the STM32 Microcontroller. There are two ADC\'92s located on the microcontroller, so I used the first ADC , and I connected the output from the sensor to it through pin A0. Then I perform the computation on the microcontroller and then the result is send to the PC using UART, where I display the heart beat live and then view the computed Beats Per Minute\
\

\f1\b Hardware/Pins \

\f2\b0 The ECG sensor outputs an analog signal, so I will use an ADC 3202/On Chip ADC, to convert the signal coming out of the ECG sensor before it is sent to the Microcontroller. \
The ECG sensor has 15 pins. I will only be using 3-pins, GND, 3.3v, output. LO-, LO+, and SDN. LO-, and LO+ are leads -off comparators, LO- is always low, and LOD+ will be high. To detect leadoff, the ECG monitors the impedance between each differential-sensing electrode and the lead-off electrode.  The impendence measurement provides an input for measuring the respiration rate. The pint OUT outputs the fully conditioned heart. Rate signal which will be connected to an ADC. The also wont be using the SDN pin, because its useful only for low-power applications. So the LO-, LO+ and OUT pins will be inputs to the PC. \
\

\f1\b Code Walkthrough
\f2\b0 \
\

\f1\b C Code:
\f2\b0 \
\pard\pardeftab720\ri-340\partightenfactor0

\f3 \cf0 In order for us to be able to time the data coming in and sample it for one minute, I used systick timer. So first of all I configure the Systick clock, by dividing the SystemCoreClocck by 1000, to transform it a millisecond delay between each consecutive ticks. Then in the SysTick Handler, I start incrementing a counter variable called myTick, that increments every millisecond. So to achieve a minute I need myTick to keep ticking until 60000, which means that I have read enough data for 1 minute. So what I do is poll for conversion using the ADC located on the micontroller and read the value from it. It reads the first sample and I have a flag which is set to one initially. Every time it detects a falling edge it is set to 1 and everytime theres a high edge higher than 2500 it is set to 0, and I do that so that I\'92d be able to get the Beats Per minute, wbich I will discuss more in details in the following sections. After that I transmit the value I received from the ADC to the terminal using UART. After I sample for one minute I transmit the beats per minute. \
\
To be able to receive the user input for samples per second and I press enter then I receive using UART interrupts in the call back function, and after that in the UART Handler, I parse , in order to be able to get the sampling rate and I send it to the systick function. If we look at the code above you can. See to sample there\'92s an if statement , and I check if myTick%samplerate ==0 then I should sample.  In the UART Handler, after I receive the read sample from the call back function, I check if there is an enter sign , once there is an enter that means I\'92ve received completely the number needed for sampling rate. Then I divide a 1000 divided by the sampling rate received as an input , I set a start flag to one which starts the ticking in the systick function and after that I start the ADC. Here I start receiving the values from the ECG. I send the flag to the systick handler, where it starts ticking, where then the reading and conversion is done, and the computations are done.\
\
\pard\pardeftab720\ri-340\partightenfactor0

\f4\b \cf0 Python Code:
\f3\b0 \
Here in the python code , I use it in order to allow users to input com port , baud rate and sampling rate. After I receive the sampling rate from the user I write it using pyserial to the microcontroller in order for me to start receiving data.  So that\'92s what I do first, I ask  for user input and then open the port. In the below code I also start setting the lists that I will use to graph. So to graph, I graph using a live plot, so as I\'92m receiving the data, I view it live, and since there are so many samples I limit the samples viewed by viewing 50 samples at a time by sliding \
\
the graph. Otherwise all the results are compressed and stuck to each other. \
In the function above, I send to it the sample rate, and I multiply it by 20%  and I append the values to a list with that size. So I\'92m doing this because when the sampling rate increased, the graph stopped updating as fast the sampling rate causing a delay and that was due to the fact that.I\'92m updating after every frame, so to solve this, instead of updating after every single sample, I append a certain number of values to the list and update them at one time.\
I call the graph function and I return it to a function called animate, and here is where I graph, by appending the y values. So what I do is receive the flag and list from the graph function, and if flag == 1 that means I should stop animating and graphing and flag is set to 1 when the word BPM is seen as an input, and I use it as my stopping condition, that if its in any of the inputs. that means I finished reading for one minute. Then I join both lists together, y2 and l2, and I set a certain length for the. size of the second list to not view all samples at the same time, and I set it as the y_axis by doing set_ydata, and I return it to the main. Then in the main I call the FuncAnimation function, which allows me to plot an animated graph. It takes my plot figure as an input the animate function, and the number of intervals. Animate does not need to be in a while loop as it keeps on calling itself until the animate function is stopped using event_source.stop(). After that I plot the. Values that I have received and I output the BPM and I\'92m done.\

\f4\b Computation:\
\pard\pardeftab720\ri-340\partightenfactor0

\f3\b0 \cf0 \
As I\'92m receiving the values from the ECG Sensor, I always check it meets a certain threshold and that their was a falling edge in the samples before it, and this way it would mean it detected a heart beat. I did this because there is a lot of noise in the middle and in order to detects a correct or almost close heart beat I always check for the rising and falling edge that meet a certain threshold, and once it is met I increment my counter until one minute is done, and then I transmit this value as my BPM. \
\uc0\u8232 
\f4\b Graphing:\uc0\u8232 
\f3\b0 In order to graph I transmit the values from the microcontroller to my python code, and then as I read each value, I append it to my list, and then I graph them. My range is between 0-4096, because the output from the ecg is ranged between those values.\
\uc0\u8232 
\f4\b User Input: 
\f3\b0 \
So first of all once you run the code, it will ask you to enter a command and in order to start, the user should enter the letter S, to indicate its time to start, after that the user should enter the COM port baud rate and the sampling rate, Once this is  done the output starts being show to the user.\
\
\
\pard\pardeftab720\ri-340\partightenfactor0

\f2 \cf0 \
}