# HPC System enabled

HPC_SYSTEMS = {

    '0': {
        'name': 'JURECA (JSC)',
        'id': 'JURECA',
        'root_url': 'https://hbp-unic.fz-juelich.de:7112/HBP_JURECA/rest/core',
        'submit_url': 'https://hbp-unic.fz-juelich.de:7112/HBP_JURECA/rest/core/jobs',
        'quota_url': 'https://hbp-unic.fz-juelich.de:7112/HBP_JURECA/rest/core/factories/default_target_system_factory',
        'system': 'UNICORE',
        'job': {
            'on_system': "{'Executable': '/bin/date', 'Resources': {'Runtime': '60'}}",
            'on_service_account': "none"
        }
    },

    '1': {
        'name': 'PIZDAINT (CSCS)',
        'id': 'PIZDAINT',
        'root_url': 'https://bspmonitors.cineca.it/pizdaint',
        'submit_url': 'https://unicoregw.cscs.ch:8080/DAINT-CSCS/rest/core/jobs',
        'quota_url': 'https://bspmonitors.cineca.it/pizdaint/projects',
        'system': 'UNICORE',
        'job': {
            'on_system': "{'Executable': '/bin/date', 'Resources': {'Runtime': '60', 'NodeConstraints': 'mc'}}",
            'on_service_account': {
                'is_link': True,
                'value': 'https://bspsa.cineca.it/jobs/pizdaint/'
            }
        }
    },

    '2': {
        'name': 'NSG',
        'id': 'NSG',
        'root_url': 'https://nsgr.sdsc.edu:8443/cipresrest/v1',
        'system': 'UNKNOWN',
        'job': {
            'on_system': 'none',
            'on_service_account': {
                'is_link': True,
                'value': 'https://bspsa.cineca.it/jobs/nsg/'
            }
        }
    }

}
