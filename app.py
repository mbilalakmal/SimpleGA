# frontend stuff

import PySimpleGUI as sg

import evaluation as ev

parameters = ['Chromosome Length'.ljust(20),
'Population Size'.ljust(20),
'Maximum Generations'.ljust(20)]

sg.theme('DarkBlue')

layout = [
    [sg.Text('')],  #padding
    [sg.Image(r'resources\icon.png'),
    sg.Text('SimpleGA', font=('Helvetica', 21))], #Title

    [sg.Text('A program for parameters evalutaion for a genetic algorithm.',
    font=('Helvetica', 12))
    ],  #subtitle

    [sg.Text('_'  * 80)],
    [sg.Text('Evaluate Parameter: '),
    sg.Combo(
        values=parameters,
        default_value=parameters[0],
        enable_events=True,
        size=(24, 4),
        font=('Helvetica', 10),
        key='_COMBO_'
    )
    ],#combobox with parameter selection
    [sg.Text('')],  #padding

    [sg.Text('Start'),
    sg.Spin([i for i in range(2,10000)], initial_value=2, size=(16,1), key='_START_')],
    [sg.Text('Stop'),
    sg.Spin([i for i in range(2,10000)], initial_value=4, size=(16,1), key='_STOP_')],
    [sg.Text('Step'),
    sg.Spin([i for i in range(1,10000)], initial_value=1, size=(16,1), key='_STEP_')],
    
    [sg.Frame(title='Other Parameters',
        layout=[
            [sg.Text(parameters[1], key='_FIRST_', font='Courier 10'),
            sg.Spin([i for i in range(2,10000)], initial_value=2, size=(12,1), key='_FIRST_VAL_')],
            [sg.Text(parameters[2], key='_SECOND_', font='Courier 10'),
            sg.Spin([i for i in range(2,10000)], initial_value=2, size=(12,1), key='_SECOND_VAL_')],
            [sg.Text('')],  #padding
            [sg.Text('Number of Trials'),
            sg.Spin([i for i in range(10,10000,10)], initial_value=10, size=(12,1), key='_TRIALS_')],
            
        ],
    )],
    [sg.Text('')],  #padding
    [sg.Button('RUN ALGORITHM')],
    [sg.Text('')],  #padding
]

window = sg.Window(
    title='Artificial Intelligence - Assignment 2',
    layout=layout,
    resizable=True,
    element_padding=(4, 4),
    element_justification='center'
    )

while True:
    event, values = window.read()
    
    if event is None:
        break

    # check if combobox selection changed
    elif event == '_COMBO_':
        
        if values['_COMBO_'] == parameters[0]:
            window['_FIRST_'].update(parameters[1])
            window['_SECOND_'].update(parameters[2])

        elif values['_COMBO_'] == parameters[1]:
            window['_FIRST_'].update(parameters[2])
            window['_SECOND_'].update(parameters[0])

        elif values['_COMBO_'] == parameters[2]:
            window['_FIRST_'].update(parameters[0])
            window['_SECOND_'].update(parameters[1])

    # check if run algorithm button is clicked
    elif event == 'RUN ALGORITHM':

        start = int(values['_START_'])
        stop = int(values['_STOP_'])
        step = int(values['_STEP_'])

        eval_parameter = values['_COMBO_']
        first_parameter = int(values['_FIRST_VAL_'])
        second_parameter = int(values['_SECOND_VAL_'])

        trials = int(values['_TRIALS_'])

        if eval_parameter == parameters[0]:
            ev.evaluate_chromosome_length(
                start=start,
                stop=stop,
                step=step,
                pop_size=first_parameter,
                max_gens=second_parameter,
                trials=trials
            )

        elif eval_parameter == parameters[1]:
            ev.evaluate_population_size(
                start=start,
                stop=stop,
                step=step,
                max_gens=first_parameter,
                chr_lnth=second_parameter,
                trials=trials
            )

        elif eval_parameter == parameters[2]:
            ev.evaluate_maximum_generations(
                start=start,
                stop=stop,
                step=step,
                chr_lnth=first_parameter,
                pop_size=second_parameter,
                trials=trials
            )

window.close()