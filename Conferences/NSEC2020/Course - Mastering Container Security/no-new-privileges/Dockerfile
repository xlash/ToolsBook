FROM ubuntu:18.04
RUN cp /bin/bash /bin/setuidbash && chmod 4755 /bin/setuidbash
RUN useradd -ms /bin/bash newuser
USER newuser
CMD ["/bin/bash"]