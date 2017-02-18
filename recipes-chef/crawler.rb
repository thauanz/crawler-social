apt_update 'Update the apt cache daily' do
  frequency 86_400
  action :periodic
end

package 'curl'

bash 'install docker' do
  code 'curl -fsSL https://get.docker.com | sh'
end

service 'docker' do
  supports :status => true
  action [:enable, :start]
end