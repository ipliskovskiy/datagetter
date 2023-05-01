# Rules

```
groups: # block with metrics
  <name_group>:
    prefix: <some_prefix> # example: mymetrics.metric.base
    metrics: # block with metrics
      <name_metrics>:
        target: # block with rules how get data
          type: <type_date>
          <specific key> # special keys it dependents of type
          ...
        sending:
          target: <type> # type stdout
        format: <format_mask>
        time: <sec> 
```

## Available targets
### math
```
target:
  type: math
  expression: ""
```

## Available ways to send data
### stdout
This is simple ways to send data. Data sending to stdout.
```
target:
  target: stdout
```

## Settings
### format
%p = groups.<name_group>.prefix
%k = groups.<name_group>.<name_metrics>
%v = The result of receiving data
