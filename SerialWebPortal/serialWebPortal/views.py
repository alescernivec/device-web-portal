from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from serialWebPortal.models import Device
from serialWebPortal.forms import DeviceForm
from django.core.urlresolvers import reverse


def index(request):
    latest_device_list = Device.objects.all()
    context = {'latest_device_list': latest_device_list}
    return render(request, 'serialWebPortal/index.html', context)

def detail(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == 'POST': 
        form = DeviceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            device.last_sent_command = cd['last_sent_command']
            device.save()
            return HttpResponseRedirect('/devices/') 
    else:
        form = DeviceForm(
            initial={'device_name': device.device_name, 
                     'device_desc': device.device_desc,
                     'create_date': device.create_date, 
                     'last_sent_command': device.last_sent_command, 
                     'rs232_settings': device.rs232_settings
                     }
        )
    return render(request, 'serialWebPortal/detail.html', {
        'form': form,'device': device
    })
    #return render(request, 'serialWebPortal/detail.html', {'device': device})

def send_message(request, device_id, message):
    device = get_object_or_404(Device, pk=device_id)
    try:
        # Tukaj pride klic na RS232
        device.last_sent_command = message
    except Exception:
        return render(request, 'serialWebPortal/detail.html', {
            'device': device,
            'error_message': "Error occured while sending message.",
        })
    else:
        device.last_sent_command = message
        device.save()
        return HttpResponseRedirect(reverse('devices:detail', args=(device.id,)))  
