{{/*
Return the chart name.
*/}}
{{- define "prometheus-url-checker.name" -}}
{{ .Chart.Name }}
{{- end }}

{{/*
Return the full name of the release.
*/}}
{{- define "prometheus-url-checker.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}

{{/*
Return chart labels.
*/}}
{{- define "prometheus-url-checker.labels" -}}
app.kubernetes.io/name: {{ include "prometheus-url-checker.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
