import textfsm


def parse_output_to_dict(template, command_output):
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
        result = fsm.ParseTextToDicts(command_output)
    return result


if __name__ == "__main__":
    with open("hua_cor_sw.config") as config:
        ports = parse_output_to_dict("templates/disp_curr_interfa.tfsm", config.read())

    for port in ports:
        print(port)
