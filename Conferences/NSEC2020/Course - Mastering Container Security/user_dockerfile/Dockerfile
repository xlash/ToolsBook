FROM ubuntu:18.04
RUN groupadd -g 999 mcsuser && \
    useradd -r -u 999 -g mcsuser mcsuser
USER mcsuser
CMD ["/bin/bash", "-c", "--", "while true; do sleep 30; done;"]