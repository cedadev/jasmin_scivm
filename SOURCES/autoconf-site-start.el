(autoload 'autoconf-mode "autoconf-mode" "Major mode for editing autoconf files." t)
(setq auto-mode-alist (cons '("\\.ac\\'\\|configure\\.in\\'" . autoconf-mode) auto-mode-alist))

(autoload 'autotest-mode "autotest-mode" "Major mode for editing autotest files." t)
(setq auto-mode-alist (cons '("\\.at\\'" . autotest-mode) auto-mode-alist))
