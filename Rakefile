require "html-proofer"

task default: %w[test]

desc "Test the HTML files"
task :test do
  options = {
    :alt_ignore => [/.*/],
    # TODO: Remove cfp.tuebix.org
    :url_ignore => [/^http:\/\/tuebix2015\.titanpad\.com/,/^\.\.\/2015\/programm\//,/^(#)$/,/cfp.tuebix.org/],
    :file_ignore => [/^_site\/201[5-7]\//],
    :typhoeus => {
      :followlocation => true,
      :connecttimeout => 30,
      :timeout => 45,
      :ssl_verifypeer => false,
      :ssl_verifyhost => 0
    }
  }
  HTMLProofer.check_directory("_site", options).run
end
